package model.ADT;

import java.util.HashMap;

public interface IFileTable<T, V> {
    V lookup(T s);

    boolean isDefined(T s);

    void update(T s, V v);

    void add(T s, V v);

    void delete(T s);

    HashMap<T, V> getContent();

}
