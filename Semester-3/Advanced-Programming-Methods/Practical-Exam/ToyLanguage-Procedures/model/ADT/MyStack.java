package model.ADT;

import model.ADT.MyIStack;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class MyStack<T> implements MyIStack<T> {
    private Stack<T> stack;
    public MyStack(Stack<T> stack) {
        this.stack = stack;
    }

    public MyStack() {
        stack = new Stack<T>();
    }

    public Stack<T> getStack() {
        return stack;
    }

    public void setStack(Stack<T> stack) {
        this.stack = stack;
    }

    public String toString() {
        return stack.toString();
    }

    @Override
    public T pop() {
        return this.stack.pop();
    }

    @Override
    public void push(T v) {
        this.stack.push(v);
    }

    @Override
    public boolean isEmpty() {
        return stack.empty();
    }

    @Override
    public List<T> getReversed() {
        List<T> list = Arrays.asList((T[]) stack.toArray());
        Collections.reverse(list);
        return list;    }

    @Override
    public T peek() {
        return this.stack.peek();
    }

    @Override
    public MyIStack<T> clone() {
        return new MyStack<T>((Stack<T>)stack.clone());
    }
}
