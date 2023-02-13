package model.stmt;

import javafx.util.Pair;
import model.ADT.IHeap;
import model.ADT.ISemaphoreTable;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.ArrayList;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CreateSemaphore implements IStmt {
    private String v;
    private Exp expression;
    private static Lock lock = new ReentrantLock();

    public CreateSemaphore(String v, Exp expression) {
        this.v = v;
        this.expression = expression;
    }


    @Override
    public String toString() {
        return "CreateSemaphore{" +
                "v='" + v + '\'' +
                ", expression=" + expression +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        IHeap heap = state.getHeap();
        ISemaphoreTable semaphoreTable = state.getSemaphoreTable();
        IntValue nr = (IntValue) (expression.eval(symTable, heap));
        int number = nr.getVal();
        int freeAddress = semaphoreTable.getFreeAddress();
        semaphoreTable.put(freeAddress, new Pair<>(number, new ArrayList<>()));
        if (symTable.isDefined(v) && symTable.lookup(v).getType().equals(new IntType()))
            symTable.update(v, new IntValue(freeAddress));
        else
            throw new MyException("Variable is not defined!");
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookup(v).equals(new IntType())) {
            if (expression.typeCheck(typeEnv).equals(new IntType())) {
                return typeEnv;
            }
            else {
                throw new MyException("Expression must be of type int!");
            }
        }
        else {
            throw new MyException("Variable must be of type int!");
        }
    }
}
