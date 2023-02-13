package model.ADT;

import java.util.HashMap;

public interface ILatchTable {
    int getFree();
    void put(int key, int value);
    int get(int key);
    boolean containsKey(int key);
    void update(int key, int value);

    void setContent(HashMap<Integer, Integer> latchTable);

    HashMap<Integer, Integer> getContent();
}
