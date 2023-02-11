#pragma once
#include "Repository.h"

class Service {
private:
	Repo* repo;

public:
	Service(Repo* repo);


	/// <summary>
	/// This function removes the patient with a given name and returns true if it exists, and false if
	/// it cannot remove the patient.
	/// </summary>
	/// <param name="name">: the given name</param>
	/// <returns></returns>
	bool removePatientServ(std::string name);

	void add5Patients();

	/// <summary>
	/// This function quarantines the infected patients and their roommates.
	/// </summary>
	void quarantinePatients();

	std::vector<Patient> getAllPatients();
};