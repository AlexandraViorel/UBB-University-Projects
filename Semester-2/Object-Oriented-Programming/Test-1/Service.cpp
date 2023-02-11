#include "Service.h"

Service::Service(Repo* repo)
{
	this->repo = repo;
}

bool Service::removePatientServ(std::string name)
{
	std::vector<Patient> v = this->repo->getPatients();

	for (int i = 0; i < v.size(); i++) {
		if (v[i].getName().compare(name) == 0) {
			if (v[i].getQuarantined() == true) {
				return false;
			}
			else {
				this->repo->removePatient(i);
				return true;
			}
		}
	}
	return false;
}

void Service::add5Patients()
{
	Patient p1 = Patient("Jessica_Thompson", 42, false, "3", false);
	Patient p2 = Patient("Lidia_Aspen", 30, true, "3", true);
	Patient p3 = Patient("Scott_Smith", 86, false, "2", false);
	Patient p4 = Patient("Zeno_Hardy", 37, true, "8", false);
	Patient p5 = Patient("Andrew_Scott", 62, false, "2", false);
	this->repo->addPatient(p1);
	this->repo->addPatient(p2);
	this->repo->addPatient(p3);
	this->repo->addPatient(p4);
	this->repo->addPatient(p5);

}

void Service::quarantinePatients()
{
	this->repo->quarantineP();
}

std::vector<Patient> Service::getAllPatients()
{
	return this->repo->getPatients();
}
