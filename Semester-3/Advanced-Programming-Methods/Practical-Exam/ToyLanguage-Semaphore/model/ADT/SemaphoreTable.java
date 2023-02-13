package model.ADT;

import javafx.util.Pair;

import java.util.HashMap;
import java.util.List;

public class SemaphoreTable implements ISemaphoreTable{
    private HashMap<Integer, Pair<Integer, List<Integer>>> semaphoreTable;
    private int freeLocation = 0;

    public SemaphoreTable() {
        this.semaphoreTable = new HashMap<>();
    }

    @Override
    public void put(int key, Pair<Integer, List<Integer>> value) {
        synchronized (this) {
            semaphoreTable.put(key, value);

        }
    }

    @Override
    public Pair<Integer, List<Integer>> get(int key){
        synchronized (this) {
            return semaphoreTable.get(key);
        }
    }

    @Override
    public boolean containsKey(int key) {
        synchronized (this) {
            return semaphoreTable.containsKey(key);
        }
    }

    @Override
    public int getFreeAddress() {
        synchronized (this) {
            freeLocation++;
            return freeLocation;
        }
    }

    @Override
    public void setFreeAddress(int freeAddress) {
        synchronized (this) {
            this.freeLocation = freeAddress;
        }
    }

    @Override
    public void update(int key, Pair<Integer, List<Integer>> value) {
        synchronized (this) {
            semaphoreTable.replace(key, value);

        }
    }

    @Override
    public HashMap<Integer, Pair<Integer, List<Integer>>> getSemaphoreTable() {
        synchronized (this) {
            return semaphoreTable;
        }
    }

    @Override
    public void setSemaphoreTable(HashMap<Integer, Pair<Integer, List<Integer>>> newSemaphoreTable) {
        synchronized (this) {
            this.semaphoreTable = newSemaphoreTable;
        }
    }

    @Override
    public String toString() {
        return semaphoreTable.toString();
    }
}
