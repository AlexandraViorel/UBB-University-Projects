package model.exp;

import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.MyException;
import model.type.Type;
import model.value.BoolValue;
import model.value.Value;

public class NotExp implements Exp{
    private Exp expression;

    public NotExp(Exp expression) {
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "!" + expression;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap heap) throws MyException {
        BoolValue value = (BoolValue) expression.eval(tbl, heap);
        if (! value.getVal()) {
            return new BoolValue(true);
        }
        else {
            return new BoolValue(false);
        }
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return expression.typeCheck(typeEnv);
    }
}
