package model.stmt;

import model.ADT.IFileTable;
import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.type.IntType;
import model.type.StringType;
import model.type.Type;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFile implements IStmt{

    private Exp exp;
    private String var_name;

    public ReadFile(Exp exp, String var_name) {
        this.exp = exp;
        this.var_name = var_name;
    }

    public Exp getExp() {
        return exp;
    }

    public void setExp(Exp exp) {
        this.exp = exp;
    }

    public String getVar_name() {
        return var_name;
    }

    public void setVar_name(String var_name) {
        this.var_name = var_name;
    }

    @Override
    public String toString() {
        return "ReadFile{" +
                "exp=" + exp +
                ", var_name='" + var_name + '\'' +
                '}';
    }


    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getSymTable().peek();
        IFileTable<String, BufferedReader> fileTable = state.getFileTable();
        IHeap heap = state.getHeap();

        if (symTable.isDefined(var_name)) {
            Value val = symTable.lookup(var_name);
            Type type = val.getType();
            if (type.equals(new IntType())) {
                StringValue value = (StringValue) exp.eval(symTable, heap);
                String file = value.getVal();
                BufferedReader f = fileTable.lookup(file);
                try {
                    String line = f.readLine();
                    if (line == null) {
                        Value v = new IntValue(0);
                        symTable.update(var_name, v);
                    }
                    else {
                        Value v = new IntValue(Integer.parseInt(line));
                        symTable.update(var_name, v);
                    }
                } catch (IOException e) {
                    System.out.println("Could not find file: " + file);
                }

            }
            else {
                throw new MyException("Type must be int!");
            }

        }

        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typeExp = exp.typeCheck(typeEnv);
        Type typeVar = typeEnv.lookup(var_name);
        if (! (typeExp.equals(new StringType()))) {
            throw new MyException("read file statement: expression type must be string!");
        }
        if (! (typeVar.equals(new IntType()))) {
            throw new MyException("read file statement: variable type must be integer!");
        }
        return typeEnv;
    }
}
