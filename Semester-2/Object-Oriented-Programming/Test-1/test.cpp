#include "test.h"
#include <cassert>

void test()
{
	Repo* repo = new Repo();
	Service* serv = new Service(repo);
	serv->add5Patients();
	serv->removePatientServ("Andrew_Scott");
	assert(serv->getAllPatients().size() == 4);
	repo->removePatient(0);
	assert(repo->getPatients().size() == 3);;
}
