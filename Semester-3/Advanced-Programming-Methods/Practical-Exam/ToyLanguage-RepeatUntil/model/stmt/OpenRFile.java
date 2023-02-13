package model.stmt;

import model.ADT.IFileTable;
import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.type.StringType;
import model.type.Type;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class OpenRFile implements IStmt{

    private Exp exp;

    public OpenRFile(Exp exp) {
        this.exp = exp;
    }

    public Exp getExp() {
        return exp;
    }

    public void setExp(Exp exp) {
        this.exp = exp;
    }

    @Override
    public String toString() {
        return "OpenRFile{" +
                "exp=" + exp +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        //MyIStack<IStmt> stk = state.getExeStack();
        MyIDictionary<String, Value> symTable = state.getSymTable();
        IFileTable<String, BufferedReader> fileTable = state.getFileTable();
        IHeap heap = state.getHeap();

        Value val = exp.eval(symTable, heap);
        if (val.getType().equals(new StringType())) {
            StringValue strVal = (StringValue) val;
            String file = strVal.getVal();
            if (fileTable.isDefined(file)) {
                throw new MyException("File already exists!");
            }
            try {
                BufferedReader r = new BufferedReader(new FileReader(file));
                fileTable.add(file, r);
            }
            catch (IOException e) {
                throw new MyException(e.getMessage());
            }
        }
        else {
            throw new MyException("Invalid type!");
        }

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type type = exp.typeCheck(typeEnv);
        if (type.equals(new StringType())) {
            return typeEnv;
        }
        else {
            throw new MyException("open file statement: expression type must be string!");
        }
    }
}
