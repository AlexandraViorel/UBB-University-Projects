package model.stmt;

import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.MyException;
import model.PrgState;
import model.type.Type;

public class Sleep implements IStmt{
    private int number;

    public Sleep(int number) {
        this.number = number;
    }

    @Override
    public String toString() {
        return "sleep(" + number + ")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        if (number != 0) {
            MyIStack<IStmt> stack = state.getExeStack();
            stack.push(new Sleep(number - 1));
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }
}
