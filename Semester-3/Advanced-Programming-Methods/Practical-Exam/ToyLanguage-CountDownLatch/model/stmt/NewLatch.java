package model.stmt;


import model.ADT.IHeap;
import model.ADT.ILatchTable;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class NewLatch implements IStmt{
    private String var;
    private Exp expression;
    private static Lock lock = new ReentrantLock();

    public NewLatch(String var, Exp expression) {
        this.var = var;
        this.expression = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        IHeap heap = state.getHeap();
        ILatchTable latchTable = state.getLatchTable();
        // we evaluate the expression in order to get its value
        IntValue nb = (IntValue) expression.eval(symTable, heap);
        int number = nb.getVal();
        // we get the free address and put the value in it
        int freeAddress = latchTable.getFree();
        latchTable.put(freeAddress, number);
        // if var is defined we update its value, and we throw an error message otherwise
        if (symTable.isDefined(var)) {
            symTable.update(var, new IntValue(freeAddress));
        }
        else {
            throw new MyException("Var is not defined!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        // both variable and expression must have type int
        if (typeEnv.lookup(var).equals(new IntType())) {
            if (expression.typeCheck(typeEnv).equals(new IntType())) {
                return typeEnv;
            }
            else {
                throw new MyException("Expression must have type int!");
            }
        }
        else {
            throw new MyException("Var must be of type int!");
        }
    }

    @Override
    public String toString() {
        return "NewLatch(" + var + ", " + expression + ")";
    }
}
