package model.stmt;

import javafx.util.Pair;
import model.ADT.IBarrierTable;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Await implements IStmt{
    private String variable;
    private static Lock lock = new ReentrantLock();

    public Await(String variable) {
        this.variable = variable;
    }

    @Override
    public String toString() {
        return "Await(" + variable + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        IBarrierTable barrierTable = state.getBarrierTable();
        if (symTable.isDefined(variable)) {
            IntValue i = (IntValue) symTable.lookup(variable);
            int foundIndex = i.getVal();
            if (barrierTable.containsKey(foundIndex)) {
                Pair<Integer, List<Integer>> foundBarrier = barrierTable.get(foundIndex);
                int NL = foundBarrier.getValue().size();
                int N1 = foundBarrier.getKey();
                ArrayList<Integer> list = (ArrayList<Integer>) foundBarrier.getValue();
                if (N1 > NL) {
                    if (list.contains(state.getId())) {
                        state.getExeStack().push(this);
                    }
                    else {
                        list.add(state.getId());
                        barrierTable.update(foundIndex, new Pair<>(N1, list));
                    }
                }
            }
            else {
                throw new MyException("Index not found in barrier table!");
            }
        }
        else {
            throw new MyException("Variable is not defined!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookup(variable).equals(new IntType())) {
            return typeEnv;
        }
        else {
            throw new MyException("Variable must be of type int!");
        }
    }
}
