package model.stmt;

import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.type.Type;

public interface IStmt {
    public PrgState execute(PrgState state) throws MyException;

    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException;
}
