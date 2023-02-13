package model.ADT;

import java.util.HashMap;

public class LockTable implements ILockTable{

    private HashMap<Integer, Integer> lockTable;
    private int freeLocation = 0;

    public LockTable() {
        lockTable = new HashMap<>();
    }


    @Override
    public int getFree() {
        freeLocation++;
        return freeLocation;
    }

    @Override
    public void put(int key, int value) {
        this.lockTable.put(key, value);
    }

    @Override
    public int get(int key) {
        return this.lockTable.get(key);
    }

    @Override
    public boolean containsKey(int key) {
        if (this.lockTable.get(key) != null) {
            return true;
        }
        else {
            return false;
        }
    }

    @Override
    public void update(int key, int value) {
        this.lockTable.put(key, value);
    }

    @Override
    public void setContent(HashMap<Integer, Integer> lockTable) {
        this.lockTable = lockTable;
    }

    @Override
    public HashMap<Integer, Integer> getContent() {
        synchronized (this) {
            return lockTable;
        }    }
}
