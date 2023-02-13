package model.value;

import model.type.StringType;
import model.type.Type;

public class StringValue implements Value{

    private String val;

    public StringValue(String val) {
        this.val = val;
    }

    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    @Override
    public String toString() {
        return val;
    }

    public boolean equals(Object another) {
        if (another instanceof StringValue)
            return true;
        else
            return false;
    }

    @Override
    public Type getType() {
        return new StringType();
    }
}
