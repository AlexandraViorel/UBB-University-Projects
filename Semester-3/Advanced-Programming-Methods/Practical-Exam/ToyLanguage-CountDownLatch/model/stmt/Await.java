package model.stmt;

import model.ADT.ILatchTable;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;
import view.Interpreter;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Await implements IStmt{
    private String var;
    private static Lock lock = new ReentrantLock();

    public Await(String var) {
        this.var = var;
    }


    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        ILatchTable latchTable = state.getLatchTable();
        // we check if var is defined and throw an error message if not
        if (symTable.isDefined(var)) {
            //we look up for the index and throw an error message if we don't find it
            IntValue index = (IntValue) symTable.lookup(var);
            int foundIndex = index.getVal();
            if (latchTable.containsKey(foundIndex)) {
                // if the index is 0 we do nothing, and if it is different from 0 we push the statement again on the
                // stack, and we must wait until the counter reach 0
                if (latchTable.get(foundIndex) != 0) {
                    state.getExeStack().push(this);
                }
            }
            else {
                throw new MyException("Index not found in latch table!");
            }
        }
        else {
            throw new MyException("Var is not defined!");
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
        return "Await(" + var + ")";
    }
}
