package model.ADT;
import javafx.util.Pair;
import model.stmt.IStmt;

import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

public class ProcTable implements IProcTable{
    private HashMap<String,  Pair<List<String>, IStmt>> procTable;

    public ProcTable() {
        this.procTable = new HashMap<>();
    }

    @Override
    public boolean isDefined(String key) {
        synchronized (this) {
            return this.procTable.containsKey(key);
        }
    }

    @Override
    public void put(String key, Pair<List<String>, IStmt> value) {
        this.procTable.put(key, value);
    }

    @Override
    public Pair<List<String>, IStmt> lookUp(String key) {
        return this.procTable.get(key);
    }

    @Override
    public void update(String key, Pair<List<String>, IStmt> value) {
        this.procTable.put(key, value);
    }

    @Override
    public Collection<Pair<List<String>, IStmt>> values() {
        synchronized (this) {
            return this.procTable.values();
        }
    }

    @Override
    public void remove(String key) {
        this.procTable.remove(key);
    }

    @Override
    public Set<String> keySet() {
        synchronized (this) {
            return procTable.keySet();
        }
    }

    @Override
    public HashMap<String, Pair<List<String>, IStmt>> getContent() {
        synchronized (this) {
            return procTable;
        }
    }

    @Override
    public MyIDictionary<String, Pair<List<String>, IStmt>> deepCopy() {
        MyIDictionary<String, Pair<List<String>, IStmt>> toReturn = new MyDictionary<>();
        for (String key: keySet())
            toReturn.add(key, lookUp(key));
        return toReturn;
    }

    @Override
    public String toString() {
        return procTable.toString();
    }
}
