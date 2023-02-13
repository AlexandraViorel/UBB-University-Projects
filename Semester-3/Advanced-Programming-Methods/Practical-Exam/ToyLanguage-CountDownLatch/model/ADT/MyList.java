package model.ADT;

import model.ADT.MyIList;

import java.util.ArrayList;
import java.util.List;

public class MyList<V> implements MyIList<V> {
    private List<V> list;

    public MyList(List<V> list) {
        this.list = list;
    }

    public List<V> getList() {
        return list;
    }

    public void setList(List<V> list) {
        this.list = list;
    }

    public String toString() {
        return list.toString();
    }

    @Override
    public void add(V value) {
        list.add(value);
    }

    public MyList() {
        this.list = new ArrayList<V>();
    }
}
