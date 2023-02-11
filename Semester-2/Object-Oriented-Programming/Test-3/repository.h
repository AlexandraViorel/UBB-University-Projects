#pragma once
#include "equation.h"
#include <vector>
#include <string>

class Repository {
private:
	std::string fileName;
	std::vector<Equation> equs;

public:
	Repository(std::string f);

	void loadFromFile();

	void addEq(Equation e);

	std::vector<Equation> getAll();
};