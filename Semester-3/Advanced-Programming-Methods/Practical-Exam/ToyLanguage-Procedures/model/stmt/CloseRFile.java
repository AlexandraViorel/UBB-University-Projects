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
import java.io.IOException;

public class CloseRFile implements IStmt{

    private Exp exp;

    public CloseRFile(Exp exp) {
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
        return "CloseRFile{" +
                "exp=" + exp +
                '}';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable().peek();
        IFileTable<String, BufferedReader> fileTable = state.getFileTable();
        IHeap heap = state.getHeap();

        Value val = exp.eval(symTable, heap);
        if (val.getType().equals(new StringType())) {
            StringValue strVal = (StringValue) val;
            String file = strVal.getVal();
            BufferedReader f = fileTable.lookup(file);
            try {
                f.close();
            } catch (IOException ex) {
                System.out.println("File " + file + " cannot be closed!");
            }
            fileTable.delete(file);
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
            throw new MyException("close file statement: the file name must have type string!");
        }
    }
}
