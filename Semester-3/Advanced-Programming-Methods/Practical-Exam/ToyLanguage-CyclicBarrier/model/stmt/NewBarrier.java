package model.stmt;

import javafx.util.Pair;
import model.ADT.IBarrierTable;
import model.ADT.IHeap;
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

public class NewBarrier implements IStmt{
    private String variable;
    private Exp expression;
    private static Lock lock = new ReentrantLock();

    public NewBarrier(String variable, Exp expression) {
        this.variable = variable;
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "NewBarrier(" + variable + ',' + expression + ')';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        lock.lock();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        IHeap heap = state.getHeap();
        IBarrierTable barrierTable = state.getBarrierTable();
        IntValue number = (IntValue) expression.eval(symTable, heap);
        int n = number.getVal();
        int freeAddr = barrierTable.getFreeAddress();
        barrierTable.put(freeAddr, new Pair<>(n, new ArrayList<>()));
        if (symTable.isDefined(variable)) {
            symTable.update(variable, new IntValue(freeAddr));
        }
        else {
            throw new MyException("Variable is not defined in the sym table!");
        }
        lock.unlock();
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if (typeEnv.lookup(variable).equals(new IntType())) {
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
