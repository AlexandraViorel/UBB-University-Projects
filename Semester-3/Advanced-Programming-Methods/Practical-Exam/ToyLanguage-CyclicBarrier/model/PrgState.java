package model;

import model.ADT.*;
import model.ADT.IFileTable;
import model.stmt.IStmt;
import model.value.Value;

import java.io.BufferedReader;

public class PrgState {
    MyIStack<IStmt> exeStack;
    MyIDictionary<String, Value> symTable;
    MyIList<Value> out;
    IFileTable<String, BufferedReader> fileTable;
    IHeap heap;

    IBarrierTable barrierTable;
    private int id;
    private static int currentId = 0;

    public PrgState(MyIStack<IStmt> stack, MyIDictionary<String, Value> symTable, MyIList<Value> list,
                    IFileTable<String, BufferedReader> fileTable, IHeap heap, IBarrierTable barrierTable, IStmt prog) {
        this.exeStack = stack;
        this.symTable = symTable;
        this.out = list;
        this.fileTable = fileTable;
        this.heap = heap;
        this.barrierTable = barrierTable;
        this.exeStack.push(prog);
        this.id = setId();
    }

    public IBarrierTable getBarrierTable() {
        return barrierTable;
    }

    public void setBarrierTable(IBarrierTable barrierTable) {
        this.barrierTable = barrierTable;
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
                "\nbarrierTable" + barrierTable + "\n\n";
    }

    public int getId() {
        return this.id;
    }
    public MyIStack<IStmt> getExeStack() {
        return exeStack;
    }

    public MyIDictionary<String, Value> getSymTable() {
        return symTable;
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

    public void setSymTable(MyIDictionary<String, Value> symTable) {
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
