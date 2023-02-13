package model.ADT;

import model.MyException;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class MyDictionary<T,V> implements MyIDictionary<T,V> {
    private HashMap<T, V> dictionary;

    public MyDictionary(HashMap<T, V> dictionary) {
        this.dictionary = dictionary;
    }

    public String toString() {
        return dictionary.toString();
    }

    @Override
    public V lookup(T s) {
        return this.dictionary.get(s);
    }

    @Override
    public boolean isDefined(T s) {
        if (this.dictionary.get(s) != null) {
            return true;
        }
        return false;
    }

    @Override
    public void update(T s, V v) {
        if (dictionary.get(s) != null) {
            this.dictionary.put(s, v);
        }
    }

    public MyDictionary() {
        this.dictionary = new HashMap<T, V>();
    }

    @Override
    public void add(T s, V v) {
        this.dictionary.putIfAbsent(s, v);
    }

    @Override
    public HashMap<T, V> getContent() {
        return this.dictionary;
    }

    @Override
    public MyIDictionary<T, V> deepCopy() {
        MyIDictionary<T, V> newDict = new MyDictionary<T, V>();
        for (Map.Entry<T, V> entry : dictionary.entrySet()) {
            newDict.add(entry.getKey(), entry.getValue());
        }
        return newDict;
    }

    @Override
    public Collection<V> values() {
        synchronized (this) {
            return this.dictionary.values();
        }
    }
}
