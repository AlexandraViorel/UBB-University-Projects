package controller;

import model.IVegetable;
import repository.IRepository;

public class Controller {
    private IRepository repository;

    public Controller(IRepository repository) {
        this.repository = repository;
    }

    public void add(IVegetable vegetable) {
        this.repository.add(vegetable);
    }

    public void remove(int position) {
        this.repository.remove(position);
    }

    public void printAll(double weight) {
        IVegetable[] vegetables = this.repository.getAll();
        for (int i = 0; i < this.repository.getSize(); i++) {
            if (vegetables[i].solve(weight)) {
                System.out.println(vegetables[i].toString());
            }
        }
    }
}
