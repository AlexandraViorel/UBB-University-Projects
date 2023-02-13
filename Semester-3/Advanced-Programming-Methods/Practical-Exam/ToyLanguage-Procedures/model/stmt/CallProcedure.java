package model.stmt;

import model.MyException;
import model.exp.Exp;
import model.PrgState;
import model.type.Type;
import model.ADT.MyDictionary;
import model.ADT.MyIDictionary;
import model.ADT.IHeap;
import model.ADT.IProcTable;
import model.value.Value;

import java.util.List;

public class CallProcedure implements IStmt{
    private String procedureName;
    private List<Exp> expressions;

    public CallProcedure(String procedureName, List<Exp> expressions) {
        this.procedureName = procedureName;
        this.expressions = expressions;
    }
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTable = state.getTopSymTable();
        IHeap heap = state.getHeap();
        IProcTable procTable = state.getProcTable();
        if (procTable.isDefined(procedureName)) {
            List<String> variables = procTable.lookUp(procedureName).getKey();
            IStmt statement = procTable.lookUp(procedureName).getValue();
            MyIDictionary<String, Value> newSymTable = new MyDictionary<>();
            for(String var: variables) {
                int ind = variables.indexOf(var);
                newSymTable.add(var, expressions.get(ind).eval(symTable, heap));
            }
            state.getSymTable().push(newSymTable);
            state.getExeStack().push(new Return());
            state.getExeStack().push(statement);
        } else {
            throw new MyException("Procedure not defined!");
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }


    @Override
    public String toString() {
        return String.format("call %s%s", procedureName, expressions.toString());
    }
}
