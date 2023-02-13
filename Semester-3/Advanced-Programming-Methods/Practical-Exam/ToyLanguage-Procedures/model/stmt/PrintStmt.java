package model.stmt;

import model.*;
import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.ADT.MyIList;
import model.ADT.MyIStack;
import model.exp.Exp;
import model.type.Type;
import model.value.Value;

public class PrintStmt implements IStmt {

    Exp exp;

    public PrintStmt(Exp exp) {
        this.exp = exp;
    }

    public Exp getExp() {
        return exp;
    }

    public void setExp(Exp exp) {
        this.exp = exp;
    }

    public String toString() {
        return "print(" + exp.toString() + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIList<Value> lst = state.getOut();
        MyIDictionary<String, Value> dict = state.getSymTable().peek();
        IHeap heap = state.getHeap();

        lst.add(exp.eval(dict, heap));
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        exp.typeCheck(typeEnv);
        return typeEnv;
    }
}
