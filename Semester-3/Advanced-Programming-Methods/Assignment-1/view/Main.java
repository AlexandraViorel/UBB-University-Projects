package view;

import controller.Controller;
import model.Eggplant;
import model.IVegetable;
import model.Pepper;
import model.Tomato;
import repository.IRepository;
import repository.Repository;

public class Main {
    public static void main(String[] args) {
        IVegetable v1 = new Tomato(0.1);
        IVegetable v2 = new Pepper(1);
        IVegetable v3 = new Eggplant(0.4);
        IVegetable v4 = new Pepper(0.199);
        IRepository repo = new Repository(3);
        Controller c = new Controller(repo);
        c.add(v1);
        c.add(v2);
        c.add(v3);
        c.add(v4);
        System.out.println("Before remove:");
        c.printAll(0.2);
        c.remove(1);
        System.out.println("After remove:");
        c.printAll(0.2);
    }
}
