package model.stmt;

import model.ADT.ILockTable;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class NewLock implements IStmt{
    private String var;
    private static Lock lock = new ReentrantLock();


    public NewLock(String var) {
        this.var = var;
    }


    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        ILockTable lockTable = state.getLockTable();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        int freeAddress = lockTable.getFree();
        lockTable.put(freeAddress, -1);
        if (symTable.isDefined(var) && symTable.lookup(var).getType().equals(new IntType())) {
            symTable.update(var, new IntValue(freeAddress));
        }
        else {
            throw new MyException("Variable not declared!");
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
            throw new MyException("Var must be of type int!");
        }
    }

    @Override
    public String toString() {
        return "NewLock(" + var + ')';
    }
}
