package model.stmt;

import model.ADT.MyIDictionary;
import model.ADT.MyIStack;
import model.MyException;
import model.PrgState;
import model.exp.Exp;
import model.exp.NotExp;
import model.type.BoolType;
import model.type.Type;

public class RepeatUntilStmt implements IStmt{
    IStmt statement;
    Exp expression;



    public RepeatUntilStmt(IStmt statement, Exp expression) {
        this.statement = statement;
        this.expression = expression;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stack = state.getExeStack();
        IStmt repeatToWhile = new CompStmt(statement, new WhileStmt(new NotExp(expression), statement));
        stack.push(repeatToWhile);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type type = expression.typeCheck(typeEnv);
        if (type.equals(new BoolType())) {
            statement.typeCheck(typeEnv.deepCopy());
            return typeEnv;
        }
        else {
            throw new MyException("Expression must be of type bool!");
        }
    }

    @Override
    public String toString() {
        return "repeat(" + statement + " ) until (" + expression + ")";
    }

}
