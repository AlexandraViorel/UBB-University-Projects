package model.stmt;

import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.ADT.MyStack;
import model.MyException;
import model.PrgState;
import model.type.Type;
import model.value.Value;

public class ForkStmt implements IStmt{
    private IStmt statement;

    public ForkStmt(IStmt statement) {
        this.statement = statement;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> newStack = new MyStack<IStmt>();
        MyIStack<MyIDictionary<String, Value>> newSymTable = state.getSymTable().clone();
        return new PrgState(newStack, newSymTable, state.getOut(), state.getFileTable(),
                state.getHeap(), state.getProcTable(), statement);
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        statement.typeCheck(typeEnv.deepCopy());
        return typeEnv;
    }

    @Override
    public String toString() {
        return "fork(" + statement.toString() + ")";
    }
}
