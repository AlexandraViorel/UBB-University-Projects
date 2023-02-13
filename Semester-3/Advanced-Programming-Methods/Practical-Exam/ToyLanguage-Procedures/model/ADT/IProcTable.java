package model.ADT;
import javafx.util.Pair;
import model.stmt.IStmt;
import java.util.*;

public interface IProcTable {
    boolean isDefined(String key);
    void put(String key, Pair<List<String>, IStmt> value);
    Pair<List<String>, IStmt> lookUp(String key);
    void update(String key,  Pair<List<String>, IStmt> value);
    Collection< Pair<List<String>, IStmt>> values();
    void remove(String key);
    Set<String> keySet();
    HashMap<String,  Pair<List<String>, IStmt>> getContent();
    MyIDictionary<String, Pair<List<String>, IStmt>> deepCopy();
}
