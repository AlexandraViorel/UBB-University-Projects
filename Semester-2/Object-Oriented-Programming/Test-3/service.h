#pragma once
#include "repository.h"

class Service {
private:
	Repository& repo;

public:
	Service(Repository& r);

	void addServ(double a, double b, double c);

	std::vector<Equation> getData();
};