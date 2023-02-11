#pragma once
#include <iostream>
#include <string>

class Equation {
private:
	double a;
	double b;
	double c;

public:
	Equation();

	Equation(double a, double b, double c);

	double getA() const;

	double getB() const;

	double getC() const;

	double getDet() const;

	std::string toString();

	friend std::istream& operator>>(std::istream& reader, Equation& eq);

};