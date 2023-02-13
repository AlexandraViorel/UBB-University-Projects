package model.stmt;

import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.type.RefType;
import model.type.Type;
import model.value.IntValue;
import model.value.RefValue;
import model.value.Value;

public class WriteHeapStmt implements IStmt{
    private String varName;
    private Exp expression;

    public WriteHeapStmt(String varName, Exp expression) {
        this.varName = varName;
        this.expression = expression;
    }

    public String getVarName() {
        return varName;
    }

    public void setVarName(String varName) {
        this.varName = varName;
    }

    public Exp getExpression() {
        return expression;
    }

    public void setExpression(Exp expression) {
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "WriteHeap("+ varName+ "," +expression + ')';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable().peek();
        IHeap heap = state.getHeap();

        Value varValue = null;
        varValue = symTable.lookup(varName);
        if (varValue == null) {
            throw new MyException("Var has not been declared!");
        }
        if (!(varValue instanceof RefValue)) {
            throw new MyException("Var should be of ref type!");
        }

        RefValue varRefValue = (RefValue) varValue;
        int heapAddr = varRefValue.getAddress();
        if (heap.get(heapAddr) == null) {
            throw new MyException("Heap addr is not valid!");
        }
        Value expValue = expression.eval(symTable, heap);
        if (! expValue.getType().equals(((RefType) varRefValue.getType()).getInner())) {
            throw new MyException("Location pointed by heap addr does not match the type of variable");
        }
        heap.update(heapAddr, expValue);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeExp = expression.typeCheck(typeEnv);
        Type typeVar = typeEnv.lookup(varName);
        if (typeVar.equals(new RefType(typeExp))) {
            return typeEnv;
        }
        else {
            throw new MyException("write heap statement: right hand side and left hand side have different types!");
        }
    }
}
