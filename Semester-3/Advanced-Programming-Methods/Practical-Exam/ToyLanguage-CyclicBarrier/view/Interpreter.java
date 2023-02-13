package view;

import controller.Controller;
import model.ADT.*;
import model.MyException;
import model.PrgState;
import model.exp.*;
import model.stmt.*;
import model.type.*;
import model.value.BoolValue;
import model.value.IntValue;
import model.value.StringValue;
import model.value.Value;
import repository.IRepository;
import repository.Repository;

import java.io.BufferedReader;
import java.util.ArrayList;

public class Interpreter {

    public static void main(String[] args) {

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));

        IStmt ex1 = new CompStmt(new VarDeclStmt("v", new IntType()),
                    new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))), new PrintStmt(new VarExp("v"))));
        try {
            ex1.typeCheck(new MyDictionary<String, Type>());
            PrgState prg1 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex1);
            ArrayList<PrgState> l1 = new ArrayList<PrgState>();
            l1.add(prg1);
            IRepository repo1 = new Repository(l1, "log1.txt");
            Controller ctr1 = new Controller(repo1);
            menu.addCommand(new RunExample("1", ex1.toString(), ctr1));
        }
        catch (MyException e) {
            System.out.println("EX 1 TYPE CHECK ERROR: " + e.getMessage());
        }


        IStmt ex2 = new CompStmt(new VarDeclStmt("a", new IntType()),
                new CompStmt(new VarDeclStmt("b", new IntType()),
                new CompStmt(new AssignStmt("a", new ArithExp("+", new ValueExp(new IntValue(2)),
                                new ArithExp("*", new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                new CompStmt(new AssignStmt("b", new ArithExp("+", new VarExp("a"),
                                        new ValueExp(new IntValue(1)))), new PrintStmt(new VarExp("b"))))));
        try {
            ex2.typeCheck(new MyDictionary<String, Type>());
            PrgState prg2 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex2);
            ArrayList<PrgState> l2 = new ArrayList<PrgState>();
            l2.add(prg2);
            IRepository repo2 = new Repository(l2, "log2.txt");
            Controller ctr2 = new Controller(repo2);
            menu.addCommand(new RunExample("2", ex2.toString(), ctr2));
        }
        catch (MyException e) {
            System.out.println("EX 2 TYPE CHECK ERROR: " + e.getMessage());
        }


        IStmt ex3 = new CompStmt(new VarDeclStmt("a", new BoolType()),
                new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),
                new CompStmt(new IfStmt(new VarExp("a"), new AssignStmt("v", new ValueExp(new IntValue(2))),
                    new AssignStmt("v", new ValueExp(new IntValue(3)))), new PrintStmt(new VarExp("v"))))));
        try {
            ex3.typeCheck(new MyDictionary<String, Type>());
            PrgState prg3 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex3);
            ArrayList<PrgState> l3 = new ArrayList<PrgState>();
            l3.add(prg3);
            IRepository repo3 = new Repository(l3, "log3.txt");
            Controller ctr3 = new Controller(repo3);
            menu.addCommand(new RunExample("3", ex3.toString(), ctr3));
        }
        catch (MyException e) {
            System.out.println("EX 3 TYPE CHECK ERROR: " + e.getMessage());
        }


        IStmt ex4 = new CompStmt(new VarDeclStmt("varf", new StringType()),
                new CompStmt(new AssignStmt("varf", new ValueExp(new StringValue("test.in"))),
                new CompStmt(new OpenRFile(new VarExp("varf")),
                new CompStmt(new VarDeclStmt("varc", new IntType()),
                new CompStmt(new ReadFile(new VarExp("varf"), "varc"),
                new CompStmt(new PrintStmt(new VarExp("varc")),
                new CompStmt(new ReadFile(new VarExp("varf"), "varc"),
                new CompStmt(new PrintStmt(new VarExp("varc")), new CloseRFile(new VarExp("varf"))))))))));
        try {
            ex4.typeCheck(new MyDictionary<String, Type>());
            PrgState prg4 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex4);
            ArrayList<PrgState> l4 = new ArrayList<PrgState>();
            l4.add(prg4);
            IRepository repo4 = new Repository(l4, "log4.txt");
            Controller ctr4 = new Controller(repo4);
            menu.addCommand(new RunExample("4", ex4.toString(), ctr4));
        }
        catch (MyException e) {
            System.out.println("EX 4 TYPE CHECK ERROR: " + e.getMessage());
        }


        IStmt ex5 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(4))),
                new CompStmt(new WhileStmt(new RelationalExp(">", new VarExp("v"), new ValueExp(new IntValue(0))),
                new CompStmt(new PrintStmt(new VarExp("v")), new AssignStmt("v", new ArithExp("-", new VarExp("v"), new ValueExp(new IntValue(1)))))),
                    new PrintStmt(new VarExp("v")))));

        try {
            ex5.typeCheck(new MyDictionary<String, Type>());
            PrgState prg5 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex5);
            ArrayList<PrgState> l5 = new ArrayList<PrgState>();
            l5.add(prg5);
            IRepository repo5 = new Repository(l5, "log5.txt");
            Controller ctr5 = new Controller(repo5);
            menu.addCommand(new RunExample("5", ex5.toString(), ctr5));
        }
        catch (MyException e) {
            System.out.println("EX 5 TYPE CHECK ERROR: " + e.getMessage());
        }


        IStmt ex6 = new CompStmt(new VarDeclStmt("v", new RefType(new IntType())),
                new CompStmt(new NewStmt("v", new ValueExp(new IntValue(20))),
                new CompStmt(new VarDeclStmt("a", new RefType(new RefType(new IntType()))),
                new CompStmt(new NewStmt("a", new VarExp("v")),
                new CompStmt(new NewStmt("v", new ValueExp(new IntValue(30))),
                        new PrintStmt(new ReadHeapExp(new ReadHeapExp(new VarExp("a")))))))));

        try {
            ex6.typeCheck(new MyDictionary<String, Type>());
            PrgState prg6 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex6);
            ArrayList<PrgState> l6 = new ArrayList<PrgState>();
            l6.add(prg6);
            IRepository repo6 = new Repository(l6, "log6.txt");
            Controller ctr6 = new Controller(repo6);
            menu.addCommand(new RunExample("6", ex6.toString(), ctr6));
        }
        catch (MyException e) {
            System.out.println("EX 6 TYPE CHECK ERROR: " + e.getMessage());

        }


        IStmt ex7 = new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new VarDeclStmt("a", new RefType(new IntType())),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(10))),
                new CompStmt(new NewStmt("a", new ValueExp(new IntValue(22))),
                new CompStmt(new ForkStmt(new CompStmt(new WriteHeapStmt("a", new ValueExp(new IntValue(30))),
                                          new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(32))),
                                          new CompStmt(new PrintStmt(new VarExp("v")), new PrintStmt(new ReadHeapExp(new VarExp("a")))
                             )))),
                new CompStmt(new PrintStmt(new VarExp("v")), new PrintStmt(new ReadHeapExp(new VarExp("a")))))))));

        try {
            ex7.typeCheck(new MyDictionary<String, Type>());
            PrgState prg7 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex7);
            ArrayList<PrgState> l7 = new ArrayList<PrgState>();
            l7.add(prg7);
            IRepository repo7 = new Repository(l7, "log7.txt");
            Controller ctr7 = new Controller(repo7);
            menu.addCommand(new RunExample("7", ex7.toString(), ctr7));
        }
        catch (MyException e) {
            System.out.println("EX 7 TYPE CHECK ERROR: " + e.getMessage());
        }

        IStmt ex8 = new CompStmt(new VarDeclStmt("v", new BoolType()),
                new CompStmt(new AssignStmt("v", new ValueExp(new IntValue(2))), new PrintStmt(new VarExp("v"))));
        try {
            ex8.typeCheck(new MyDictionary<String, Type>());
            PrgState prg8 = new PrgState(new MyStack<IStmt>(), new MyDictionary<String, Value>(), new MyList<Value>(),
                    new FileTable<String, BufferedReader>(), new Heap(), new BarrierTable(), ex8);
            ArrayList<PrgState> l8 = new ArrayList<PrgState>();
            l8.add(prg8);
            IRepository repo8 = new Repository(l8, "log8.txt");
            Controller ctr8 = new Controller(repo8);
            menu.addCommand(new RunExample("8", ex8.toString(), ctr8));
        }
        catch (MyException e) {
            System.out.println("EX 8 TYPE CHECK ERROR: " + e.getMessage());
        }

        menu.show();

    }
}
