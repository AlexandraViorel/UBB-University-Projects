package model.exp;

import model.*;
import model.ADT.IHeap;
import model.ADT.MyIDictionary;
import model.type.IntType;
import model.type.Type;
import model.value.IntValue;
import model.value.Value;

public class ArithExp implements Exp {
    private Exp e1;
    private Exp e2;
    private int op; // 1 - plus, 2 - minus, 3 - star, 4 - divide

    public ArithExp(String stringOp, Exp e1, Exp e2) {
        this.e1 = e1;
        this.e2 = e2;
        switch (stringOp) {
            case "+" -> op = 1;
            case "-" -> op = 2;
            case "*" -> op = 3;
            case "/" -> op = 4;
        }
    }

    public Exp getE1() {
        return e1;
    }

    public void setE1(Exp e1) {
        this.e1 = e1;
    }

    public Exp getE2() {
        return e2;
    }

    public void setE2(Exp e2) {
        this.e2 = e2;
    }

    public int getOp() {
        return op;
    }

    public void setOp(int op) {
        this.op = op;
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, IHeap heap) throws MyException {
        Value v1, v2;
        v1 = e1.eval(tbl, heap);
        if (v1.getType().equals(new IntType())) {
            v2 = e2.eval(tbl, heap);
            if (v2.getType().equals(new IntType())) {
                IntValue i1 = (IntValue) v1;
                IntValue i2 = (IntValue) v2;
                int n1, n2;
                n1 = i1.getVal();
                n2 = i2.getVal();
                if (op == 1) return new IntValue(n1 + n2);
                if (op == 2) return new IntValue(n1 - n2);
                if (op == 3) return new IntValue(n1 * n2);
                if (op == 4)
                    if (n2 == 0) throw new MyException("division by zero");
                    else return new IntValue(n1 / n2);
            } else {
                throw new MyException("second operand is not an integer");
            }
        } else {
            throw new MyException("first operand is not an integer");
        }
        return null;
    }

    @Override
    public Type typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typ1, typ2;
        typ1 = e1.typeCheck(typeEnv);
        typ2 = e2.typeCheck(typeEnv);
        if (typ1.equals(new IntType())) {
            if (typ2.equals(new IntType())) {
                return new IntType();
            }
            else {
                throw new MyException("second operand is not an integer");
            }
        }
        else {
            throw new MyException("first operand is not an integer");
        }
    }

    @Override
    public String toString() {
        return "ArithExp{" +
                "e1=" + e1 +
                ", e2=" + e2 +
                ", op=" + op +
                '}';
    }
}
