package controller;

import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.stmt.IStmt;
import model.MyException;
import model.ADT.MyIStack;
import model.PrgState;
import model.value.RefValue;
import model.value.Value;
import repository.IRepository;

import java.util.*;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Controller {
    private IRepository repository;

    private ExecutorService executor;

    public Controller(IRepository repository) {
        this.repository = repository;
    }

    public IRepository getRepository() {
        return repository;
    }

    public void setRepository(IRepository repository) {
        this.repository = repository;
    }

    public List<PrgState> getProgramStates() {
        return repository.getPrgList();
    }

    public void setProgramStates(List<PrgState> prgStates) {
        repository.setPrgList(prgStates);
    }

    private List<Integer> getAddrFromSymTable(Collection<Value> symTableValues) {
        return symTableValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue)v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    private List<Integer> getAddrFromHeap(Collection<Value> heapValues) {
        return heapValues.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue)v; return v1.getAddress();})
                .collect(Collectors.toList());
    }

    private Map<Integer, Value> unsafeGarbageCollector(List<Integer> symTableAddr, Map<Integer, Value> heap) {
        return heap.entrySet().stream()
                .filter(e -> symTableAddr.contains(e.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    private Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddr, Map<Integer, Value> heap) {
        List<Integer> heapAddr = getAddrFromHeap(heap.values());
        return heap.entrySet().stream()
                .filter(e -> (symTableAddr.contains(e.getKey()) || heapAddr.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public void allStep() throws InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        // remove completed programs
        List<PrgState> prgList = removeCompletedPrg(repository.getPrgList());
        while (prgList.size() > 0) {
            // safe garbage collector
            IHeap sharedHeap = prgList.get(0).getHeap();
            List<MyIDictionary<String, Value>> allSymTables = prgList.stream()
                    .map(PrgState::getSymTable)
                    .collect(Collectors.toList());

            List<Integer> addressesFromAllSymTables = new ArrayList<Integer>();
            allSymTables.stream()
                    .map(table -> getAddrFromSymTable(table.getContent().values()))
                    .forEach(addressesFromAllSymTables::addAll);

            sharedHeap.setContent((HashMap<Integer, Value>) safeGarbageCollector(addressesFromAllSymTables,
                    sharedHeap.getContent()));

            // finish safe garbage collector
            oneStepForAllPrg(prgList);
            // remove the completed programs
            prgList = removeCompletedPrg(repository.getPrgList());
        }
        executor.shutdownNow();
        //update the repository state
        repository.setPrgList(prgList);
    }

    public List<PrgState> removeCompletedPrg(List<PrgState> inPrgList) {
        return inPrgList.stream()
                .filter(p -> p.isNotCompleted())
                .collect(Collectors.toList());
    }

    public void oneStepForAllPrg(List<PrgState> prgList) throws InterruptedException {
        // before the execution, print the prg state list into the log file
        prgList.forEach(prg -> {
            try {
                repository.logPrgStateExec(prg);
            } catch (MyException e) {
                throw new RuntimeException(e);
            }
        });
        // run concurrently one step for each of the existing prg states
        //prepare the list of callables
        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>) (() -> {return p.oneStep();}))
                .collect(Collectors.toList());

        // start the execution of the callables
        // it returns the list of new created prg states (namely threads)
        List<PrgState> newPrgList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (InterruptedException | ExecutionException exception) {
                        throw new RuntimeException(exception);
                    }
                })
                .filter(p -> p != null)
                .collect(Collectors.toList());

        // add the new created threads to the list of existing threads
        prgList.addAll(newPrgList);

        // after the execution, print the prg state list into the log file
        prgList.forEach(prg -> {
            try {
                repository.logPrgStateExec(prg);
            } catch (MyException e) {
                throw new RuntimeException(e);
            }
        });

        // save the current programs in the repository
        repository.setPrgList(prgList);
    }

    public void conservativeGarbageCollector(List<PrgState> programStates) {
        List<Integer> symTableAddresses = Objects.requireNonNull(programStates.stream()
                        .map(p -> getAddrFromSymTable(p.getSymTable().values()))
                        .map(Collection::stream)
                        .reduce(Stream::concat).orElse(null))
                        .collect(Collectors.toList());
        programStates.forEach(p -> p.getHeap().setContent((HashMap<Integer, Value>) safeGarbageCollector(symTableAddresses, p.getHeap().getContent())));
    }

    public void oneStep() throws InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        List<PrgState> programStates = removeCompletedPrg(repository.getPrgList());
        oneStepForAllPrg(programStates);
        conservativeGarbageCollector(programStates);
        executor.shutdownNow();
    }
}
