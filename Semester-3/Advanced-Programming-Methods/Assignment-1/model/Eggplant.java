package model;

public class Eggplant implements IVegetable {
    private double weight;

    public Eggplant(double weight) {
        this.weight = weight;
    }

    public String toString() {
        return "Eggplant, weight: " + this.weight;
    }

    @Override
    public boolean solve(double weight) {
        if (this.weight > weight) {
            return true;
        }
        return false;
    }
}
