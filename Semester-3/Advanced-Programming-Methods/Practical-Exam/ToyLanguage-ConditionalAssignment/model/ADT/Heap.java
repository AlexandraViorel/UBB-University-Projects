package model.ADT;

import model.value.Value;

import java.util.HashMap;

public class Heap implements IHeap{
    private HashMap<Integer, Value> heapTable;
    private int freeLocation;

    public Heap() {
        this.heapTable = new HashMap<Integer, Value>();
        this.freeLocation = 0;
    }

    public void setFreeLocation(int freeLocation) {
        this.freeLocation = freeLocation;
    }

    @Override
    public void put(int key, Value value) {
        heapTable.put(key, value);
    }

    @Override
    public Value get(int key) {
        return heapTable.get(key);
    }

    @Override
    public boolean containsKey(int key) {
        if (this.heapTable.get(key) != null) {
            return true;
        }
        else {
            return false;
        }
    }

    @Override
    public void update(int key, Value value) {
        this.heapTable.put(key, value);
    }

    @Override
    public int getFreeAddress() {
        freeLocation++;
        return freeLocation;
    }

    @Override
    public void setContent(HashMap<Integer, Value> heap) {
        this.heapTable = heap;
    }

    @Override
    public HashMap<Integer, Value> getContent() {
        return heapTable;
    }

    @Override
    public String toString() {
        return heapTable.toString();
    }
}
