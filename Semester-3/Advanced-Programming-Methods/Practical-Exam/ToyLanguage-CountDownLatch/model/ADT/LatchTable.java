package model.ADT;

import java.util.HashMap;

public class LatchTable implements ILatchTable{
    private HashMap<Integer, Integer> latchTable;
    private int freeLocation = 0;

    public LatchTable() {
        latchTable = new HashMap<>();
    }

    @Override
    public String toString() {
        return latchTable.toString();
    }

    @Override
    public int getFree() {
        synchronized (this) {
            freeLocation++;
            return freeLocation;
        }

    }

    @Override
    public void put(int key, int value) {
        synchronized (this) {
            this.latchTable.put(key, value);

        }

    }

    @Override
    public int get(int key) {
        synchronized (this) {
            return this.latchTable.get(key);

        }

    }

    @Override
    public boolean containsKey(int key) {
        synchronized (this) {
            if (this.latchTable.get(key) != null) {
                return true;
            }
            else {
                return false;
            }
        }

    }

    @Override
    public void update(int key, int value) {
        synchronized (this) {
            this.latchTable.put(key, value);
        }
    }

    @Override
    public void setContent(HashMap<Integer, Integer> latchTable) {
        synchronized (this) {
            this.latchTable = latchTable;
        }

    }

    @Override
    public HashMap<Integer, Integer> getContent() {
        synchronized (this) {
            return latchTable;
        }    }
}
