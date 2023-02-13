package model;

public class Tomato implements IVegetable {
    private double weight;

    public Tomato(double weight) {
        this.weight = weight;
    }

    public String toString() {
        return "Tomato, weight: " + this.weight;
    }

    @Override
    public boolean solve(double weight) {
        if (this.weight > weight) {
            return true;
        }
        return false;
    }
}
