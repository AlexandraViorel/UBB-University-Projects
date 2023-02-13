package model.stmt;

import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.MyException;
import model.PrgState;
import model.exp.ValueExp;
import model.type.Type;
import model.value.IntValue;

public class Wait implements IStmt{
    private int number;

    public Wait(int number) {
        this.number = number;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        if (number != 0) {
            MyIStack<IStmt> stack = state.getExeStack();
            stack.push(new CompStmt(new PrintStmt(new ValueExp(new IntValue(number))), new Wait(number - 1)));
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    @Override
    public String toString() {
        return "Wait(" + number + ")";
    }
}
