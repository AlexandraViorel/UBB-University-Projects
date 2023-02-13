package model.stmt;

import model.*;
import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.exp.Exp;
import model.type.Type;
import model.value.Value;

public class AssignStmt implements IStmt {

    private String id;
    private Exp exp;

    public AssignStmt(String id, Exp exp) {
        this.id = id;
        this.exp = exp;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Exp getExp() {
        return exp;
    }

    public void setExp(Exp exp) {
        this.exp = exp;
    }

    public String toString() {
        return id + "=" + exp.toString();
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        IHeap heap = state.getHeap();

        if (symTable.isDefined(id)) {
            Value val = exp.eval(symTable, heap);
            Type typId = (symTable.lookup(id)).getType();
            if (val.getType().equals(typId)) {
                symTable.update(id, val);
            }
            else {
                throw new MyException("declared type of variable " + id + " any type of the assigned expression do not " +
                        "match");
            }
        }
        else {
            throw new MyException("the used variable " + id + " was not declared before");
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeVar = typeEnv.lookup(id);
        Type typeExp = exp.typeCheck(typeEnv);
        if (typeVar.equals(typeExp)) {
            return typeEnv;
        }
        else {
            throw new MyException("assignment statement: right hand side and left hand side have different types!");
        }
    }
}
