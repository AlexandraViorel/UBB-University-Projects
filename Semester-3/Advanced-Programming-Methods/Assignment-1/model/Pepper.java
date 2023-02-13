package model;

public class Pepper implements IVegetable {
    private double weight;

    public Pepper(double weight) {
        this.weight = weight;
    }

    public String toString() {
        return "Pepper, weight: " + this.weight;
    }

    @Override
    public boolean solve(double weight) {
        if (this.weight > weight) {
            return true;
        }
        return false;
    }
}
