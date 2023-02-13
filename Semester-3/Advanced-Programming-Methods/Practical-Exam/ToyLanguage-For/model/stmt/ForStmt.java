package model.stmt;

import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.exp.RelationalExp;
import model.exp.VarExp;
import model.type.BoolType;
import model.type.IntType;
import model.type.Type;

public class ForStmt implements IStmt{

    private IStmt statement;
    private String string;
    private Exp expression1;
    private Exp expression2;
    private Exp expression3;

    public ForStmt(IStmt statement, String string, Exp expression1, Exp expression2, Exp expression3) {
        this.statement = statement;
        this.string = string;
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.expression3 = expression3;
    }


    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stack = state.getExeStack();
        IStmt forToWhile = new CompStmt(new AssignStmt(string, expression1),
                           new WhileStmt(new RelationalExp("<", new VarExp(string), expression2),
                                   new CompStmt(statement, new AssignStmt(string, expression3))));
        stack.push(forToWhile);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type type1 = expression1.typeCheck(typeEnv);
        Type type2 = expression2.typeCheck(typeEnv);
        Type type3 = expression3.typeCheck(typeEnv);
        if (type1.equals(new IntType()) && type2.equals(new IntType()) && type3.equals(new IntType())) {
            return typeEnv;
        }
        else {
            throw new MyException("For statement has wrong types! All must be int!");
        }
    }

    @Override
    public String toString() {
        return "for(" + string + "=" + expression1 + "; " + string + "<" + expression2 + "; " + string + "=" +
                expression3 + ") { " + statement + "}";
    }
}
