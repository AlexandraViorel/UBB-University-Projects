package model.exp;

import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.MyException;
import model.type.IntType;
import model.type.Type;
import model.value.Value;

public class MULExp implements Exp{
    private Exp exp1;
    private Exp exp2;

    public MULExp(Exp exp1, Exp exp2) {
        this.exp1 = exp1;
        this.exp2 = exp2;
    }

    public Exp getExp1() {
        return exp1;
    }

    public void setExp1(Exp exp1) {
        this.exp1 = exp1;
    }

    public Exp getExp2() {
        return exp2;
    }

    public void setExp2(Exp exp2) {
        this.exp2 = exp2;
    }

    @Override
    public String toString() {
        return "MULExp{" +
                "exp1=" + exp1 +
                ", exp2=" + exp2 +
                '}';
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap heap) throws MyException {
        Exp converted = new ArithExp("-", new ArithExp("*", exp1, exp2), new ArithExp("+", exp1, exp2));
        return converted.eval(tbl, heap);
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type type1 = exp1.typeCheck(typeEnv);
        Type type2 = exp2.typeCheck(typeEnv);
        if (type1.equals(new IntType()) && type2.equals(new IntType())) {
            return new IntType();
        }
        else {
            throw new MyException("Expressions in MUL must be of type int!");
        }
    }
}
