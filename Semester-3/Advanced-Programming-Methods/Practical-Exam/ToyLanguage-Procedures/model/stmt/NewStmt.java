package model.stmt;

import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.type.RefType;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;

public class NewStmt implements IStmt{
    private String varName;
    private Exp expression;

    public NewStmt(String varName, Exp expression) {
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
        return "new(" + varName + "," + expression.toString() + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable().peek();
        IHeap heap = state.getHeap();

        Value val = symTable.lookup(varName);
        if (val == null) {
            throw new MyException("Variable was not defined!");
        }
        if (!(val instanceof RefValue)) {
            throw new MyException("Variable must be of RefType!");
        }

        Value expV = expression.eval(symTable, heap);
        Type locationType = ((RefType) val.getType()).getInner();

        if (! (expV.getType().equals(locationType))) {
            throw new MyException("Reference location type does not match expression type!");
        }

        int heapAddr = heap.getFreeAddress();
        heap.put(heapAddr, expV);
        RefValue refV = (RefValue) val;
        RefValue newRef = new RefValue(heapAddr, ((RefType) refV.getType()).getInner());
        symTable.update(varName, newRef);

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeVar = typeEnv.lookup(varName);
        Type typeExp = expression.typeCheck(typeEnv);
        if (typeVar.equals(new RefType(typeExp))) {
            return typeEnv;
        }
        else {
            throw new MyException("new statement: right hand side and left hand side have different types!");
        }
    }
}
