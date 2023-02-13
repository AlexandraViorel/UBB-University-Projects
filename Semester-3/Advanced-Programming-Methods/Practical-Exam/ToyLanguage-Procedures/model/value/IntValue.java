package model.value;

import model.type.IntType;
import model.type.StringType;
import model.type.Type;

public class IntValue implements Value {
    private int val;

    public IntValue(int val) {
        this.val = val;
    }

    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }

    @Override
    public String toString() {
        return Integer.toString(val);
    }

    public boolean equals(Object another) {
        if (another instanceof IntValue)
            return true;
        else
            return false;
    }

    @Override
    public Type getType() {
        return new IntType();
    }
}
