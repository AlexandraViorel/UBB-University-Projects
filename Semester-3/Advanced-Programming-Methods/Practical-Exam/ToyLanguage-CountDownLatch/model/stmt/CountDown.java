package model.stmt;


import model.ADT.ILatchTable;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.exp.ValueExp;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CountDown implements IStmt{
    private String var;
    private static Lock lock = new ReentrantLock();

    public CountDown(String var) {
        this.var = var;
    }


    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        ILatchTable latchTable = state.getLatchTable();
        // we check if v was defined in the sym table, if not we throw an error message
        if (symTable.isDefined(var)) {
            // we look up for the index and if we don't find it in the latch table we throw an error message
            IntValue index = (IntValue) symTable.lookup(var);
            int foundIndex = index.getVal();
            if (latchTable.containsKey(foundIndex)) {
                // if the found index is greater than 0, we decrease it with 1, else we print the prg state id
                if (latchTable.get(foundIndex) > 0) {
                    latchTable.update(foundIndex, latchTable.get(foundIndex) - 1);
                }
                state.getExeStack().push(new PrintStmt(new ValueExp(new IntValue(state.getId()))));
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
        return "CountDown(" + var + ")";
    }
}
