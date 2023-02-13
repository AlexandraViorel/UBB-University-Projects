package model;

import model.ADT.*;
import model.ADT.IFileTable;
import model.stmt.IStmt;
import model.value.Value;

import java.io.BufferedReader;

public class PrgState {
    MyIStack<IStmt> exeStack;
    MyIStack<MyIDictionary<String, Value>> symTable;

    MyIList<Value> out;
    IFileTable<String, BufferedReader> fileTable;
    IHeap heap;
    IProcTable procTable;
    private int id;
    private static int currentId = 0;

    public PrgState(MyIStack<IStmt> stack, MyIStack<MyIDictionary<String, Value>> symTable, MyIList<Value> list,
                    IFileTable<String, BufferedReader> fileTable, IHeap heap, IProcTable procTable, IStmt prog) {
        this.exeStack = stack;
        this.symTable = symTable;
        this.out = list;
        this.fileTable = fileTable;
        this.heap = heap;
        this.procTable = procTable;
        this.exeStack.push(prog);
        this.id = setId();
    }

    public IProcTable getProcTable() {
        return procTable;
    }

    public void setProcTable(IProcTable procTable) {
        this.procTable = procTable;
    }

    @Override
    public String toString() {
        return "Program State : \n\n" +
                "id = " + id +
                "\nexeStack = " + exeStack +
                "\nsymTable=" + symTable +
                "\nout=" + out +
                "\nfileTable=" + fileTable +
                "\nheap=" + heap +
                "\nprocTable=" + procTable + "\n\n";
    }

    public int getId() {
        return this.id;
    }
    public MyIStack<IStmt> getExeStack() {
        return exeStack;
    }

    public MyIStack<MyIDictionary<String, Value>> getSymTable() {
        return symTable;
    }

    public MyIDictionary<String, Value> getTopSymTable() {
        return symTable.peek();
    }

    public MyIList<Value> getOut() {
        return out;
    }

    public IFileTable<String, BufferedReader> getFileTable() {
        return fileTable;
    }

    public void setExeStack(MyIStack<IStmt> exeStack) {
        this.exeStack = exeStack;
    }

    public void setSymTable(MyIStack<MyIDictionary<String, Value>> symTable) {
        this.symTable = symTable;
    }

    public void setOut(MyIList<Value> out) {
        this.out = out;
    }

    public void setFileTable(IFileTable<String, BufferedReader> fileTable) {
        this.fileTable = fileTable;
    }

    public IHeap getHeap() {
        return heap;
    }

    public void setHeap(IHeap heap) {
        this.heap = heap;
    }

    public synchronized int setId() {
        currentId++;
        return currentId;
    }
    public Boolean isNotCompleted() {
        if (! exeStack.isEmpty()) {
            return true;
        }
        else {
            return false;
        }
    }

    public PrgState oneStep() throws MyException {
        if (exeStack.isEmpty()) throw new MyException("Program state stack is empty!");
        IStmt currentStatement = exeStack.pop();
        return currentStatement.execute(this);
    }
}
