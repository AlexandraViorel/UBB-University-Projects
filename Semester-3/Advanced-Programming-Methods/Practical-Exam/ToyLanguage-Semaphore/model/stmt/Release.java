package model.stmt;

import javafx.util.Pair;
import model.ADT.ISemaphoreTable;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.List;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Release implements IStmt{
    private String var;
    private static Lock lock = new ReentrantLock();

    public Release(String var) {
        this.var = var;
    }

    @Override
    public String toString() {
        return "Release{" +
                "var='" + var + '\'' +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        ISemaphoreTable semaphoreTable = state.getSemaphoreTable();
        if (symTable.isDefined(var)) {
            if (symTable.lookup(var).getType().equals(new IntType())) {
                IntValue fi = (IntValue) symTable.lookup(var);
                int foundIndex = fi.getVal();
                if (semaphoreTable.getSemaphoreTable().containsKey(foundIndex)) {
                    Pair<Integer, List<Integer>> foundSemaphore = semaphoreTable.get(foundIndex);
                    if (foundSemaphore.getValue().contains(state.getId()))
                        foundSemaphore.getValue().remove((Integer) state.getId());
                    semaphoreTable.update(foundIndex, new Pair<>(foundSemaphore.getKey(), foundSemaphore.getValue()));
                } else {
                    throw new MyException("Index not in the semaphore table!");
                }
            } else {
                throw new MyException("Index must be of int type!");
            }
        } else {
            throw new MyException("Index not in symbol table!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookup(var).equals(new IntType())) {
            return typeEnv;
        }
        else {
            throw new MyException("Variable must be of type int!");
        }
    }
}
