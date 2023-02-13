package repository;

import model.IVegetable;

public interface IRepository {
    public void add(IVegetable vegetable);

    public void remove(int position);

    public IVegetable[] getAll();

    public int getSize();
}
