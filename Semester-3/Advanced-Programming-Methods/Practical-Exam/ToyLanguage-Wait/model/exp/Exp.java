package model.exp;

import model.ADT.IHeap;
import model.MyException;
import model.ADT.MyIDictionary;
import model.type.Type;
import model.value.Value;

public interface Exp {
    Value eval(MyIDictionary<String, Value> tbl, IHeap heap) throws MyException;

    Type typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException;
}
