package model.value;

import model.type.BoolType;
import model.type.StringType;
import model.type.Type;

public class BoolValue implements Value {
    private boolean val;

    public BoolValue(boolean val) {
        this.val = val;
    }

    public boolean getVal() {
        return val;
    }

    public void setVal(boolean val) {
        this.val = val;
    }

    @Override
    public String toString() {
        return Boolean.toString(val);
    }

    public boolean equals(Object another) {
        if (another instanceof BoolValue)
            return true;
        else
            return false;
    }

    @Override
    public Type getType() {
        return new BoolType();
    }
}
