package repository;

import model.IVegetable;

public class Repository implements IRepository{
    private IVegetable[] vegetables;
    private int size;

    public Repository(int maxSize) {
        this.size = 0;
        this.vegetables = new IVegetable[maxSize];
    }

    public int getSize() {
        return size;
    }

    public void add(IVegetable vegetable) {
        try {
            this.vegetables[this.size] = vegetable;
            this.size++;
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    public void remove(int position) {
        if (position < this.size) {
            IVegetable[] newVegetables = new IVegetable[this.size - 1];
            int newSize = 0;
            for (int i = 0; i < this.size; i++) {
                if (i != position) {
                    newVegetables[newSize] = this.vegetables[i];
                    newSize++;
                }
            }
            this.vegetables = newVegetables;
            this.size = newSize;
        } else {
            System.out.println("Position does not exist!");
        }
    }

    public IVegetable[] getAll() {
        return this.vegetables;
    }
}
