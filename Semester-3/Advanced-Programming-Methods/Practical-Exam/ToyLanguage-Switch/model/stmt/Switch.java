package model.stmt;

import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.exp.RelationalExp;
import model.type.Type;

public class Switch implements IStmt{
    private Exp exp;
    private Exp exp1;
    private IStmt stmt1;
    private Exp exp2;
    private IStmt stmt2;
    private IStmt stmt3;



    public Switch(Exp exp, Exp exp1, IStmt stmt1, Exp exp2, IStmt stmt2, IStmt stmt3) {
        this.exp = exp;
        this.exp1 = exp1;
        this.stmt1 = stmt1;
        this.exp2 = exp2;
        this.stmt2 = stmt2;
        this.stmt3 = stmt3;
    }

    @Override
    public String toString() {
        return "Switch(" + exp +
                ") (case " + exp1 +
                ": " + stmt1 +
                ") (case " + exp2 +
                ": " + stmt2 +
                ") (default: " + stmt3 +
                ')';
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stack = state.getExeStack();
        IStmt converted = new IfStmt(new RelationalExp("==", exp, exp1), stmt1,
                new IfStmt(new RelationalExp("==", exp, exp2), stmt2, stmt3));
        stack.push(converted);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type type = exp.typeCheck(typeEnv);
        Type type1 = exp1.typeCheck(typeEnv);
        Type type2 = exp2.typeCheck(typeEnv);
        if (type.equals(type1) && type.equals(type2)) {
            stmt1.typeCheck(typeEnv.deepCopy());
            stmt2.typeCheck(typeEnv.deepCopy());
            stmt3.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else {
            throw new MyException("The expression types do not match in the switch statement!");
        }
    }
}
