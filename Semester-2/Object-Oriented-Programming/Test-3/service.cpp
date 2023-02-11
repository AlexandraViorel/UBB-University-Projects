#include "service.h"

Service::Service(Repository& r) : repo{ r }
{
}

void Service::addServ(double a, double b, double c)
{
	Equation eq{ a, b, c };
	this->repo.addEq(eq);
}

std::vector<Equation> Service::getData()
{
	return this->repo.getAll();
}
