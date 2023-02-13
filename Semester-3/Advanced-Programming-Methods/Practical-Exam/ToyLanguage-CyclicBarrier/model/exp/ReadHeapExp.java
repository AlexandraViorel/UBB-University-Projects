package model.exp;

import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.MyException;
import model.type.RefType;
import model.type.Type;
import model.value.RefValue;
import model.value.Value;

public class ReadHeapExp implements Exp{
    Exp expression;

    public ReadHeapExp(Exp expression) {
        this.expression = expression;
    }

    public Exp getExpression() {
        return expression;
    }

    public void setExpression(Exp expression) {
        this.expression = expression;
    }

    @Override
    public String toString() {
        return "ReadHeapExp(" +
                "exp=" + expression +
                ')';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap heap) throws MyException {
        Value v = expression.eval(tbl, heap);
        if (v instanceof RefValue) {
            RefValue refValue = (RefValue) v;
            int addr = refValue.getAddress();
            if (heap.containsKey(addr)) {
                return heap.get(addr);
            }
            else {
                throw new MyException("location does not exist!");
            }
        }
        else {
            throw new MyException("expression must be RefValue");
        }
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typ = expression.typeCheck(typeEnv);
        if (typ instanceof RefType) {
            RefType reft = (RefType) typ;
            return reft.getInner();
        }
        else {
            throw new MyException("the rH argument is not a RefType!");
        }
    }
}
