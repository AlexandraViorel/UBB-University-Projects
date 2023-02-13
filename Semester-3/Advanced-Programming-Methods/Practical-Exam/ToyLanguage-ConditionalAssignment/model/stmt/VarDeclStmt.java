package model.stmt;

import model.*;
import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.type.Type;
import model.value.Value;

public class VarDeclStmt implements IStmt {
    private String name;
    private Type type;

    public VarDeclStmt(String name, Type type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTbl = state.getSymTable();
        if (symTbl.isDefined(name)) {
            throw new MyException("variable is already defined");
        }
        else {
            symTbl.add(name, type.defaultValue());
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        typeEnv.add(name, type);
        return typeEnv;
    }

    @Override
    public String toString() {
        return "VarDeclStmt{" +
                "name='" + name + '\'' +
                ", type=" + type +
                '}';
    }
}