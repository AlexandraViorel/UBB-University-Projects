#pragma once
#include <vector>
#include "Domain.h"

class Repo {
private:
	std::vector<Patient> elems;
public:
	Repo();

	void addPatient(Patient p);

	/// <summary>
	/// This function removes the patient on the given position.
	/// </summary>
	/// <param name="position">: the given pos</param>
	void removePatient(int position);


	void quarantineP();
	std::vector<Patient> getPatients();
};