package model.ADT;

import java.util.Collection;
import java.util.HashMap;

public interface MyIDictionary<T,V> {

    V lookup(T s);

    boolean isDefined(T s);

    void update(T s, V v);

    void add(T s, V v);

    HashMap<T, V> getContent();

    MyIDictionary<T, V> deepCopy();

    Collection<V> values();
}
