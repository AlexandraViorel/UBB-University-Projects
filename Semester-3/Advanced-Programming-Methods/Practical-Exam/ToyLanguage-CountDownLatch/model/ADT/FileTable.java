package model.ADT;

import java.util.HashMap;

public class FileTable<T, V> implements IFileTable<T, V>{
    private HashMap<T, V> dictionary;

    public FileTable(HashMap<T, V> dictionary) {
        this.dictionary = dictionary;
    }

    public HashMap<T, V> getDictionary() {
        return dictionary;
    }

    public void setDictionary(HashMap<T, V> dictionary) {
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

    @Override
    public void add(T s, V v) {
        this.dictionary.putIfAbsent(s, v);
    }

    @Override
    public void delete(T s) {
        dictionary.remove(s);
    }

    @Override
    public HashMap<T, V> getContent() {
        return this.dictionary;
    }

    public FileTable() {
        this.dictionary = new HashMap<T, V>();
    }
}
