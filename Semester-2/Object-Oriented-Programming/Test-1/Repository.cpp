#include "Repository.h"

Repo::Repo()
{
}

void Repo::addPatient(Patient p)
{
	this->elems.push_back(p);
}

void Repo::removePatient(int position)
{
	this->elems.erase(elems.begin() + position);
}

void Repo::quarantineP()
{
	std::vector<std::string> quarantinedRooms;
	for (int i = 0; i < this->elems.size(); i++) {
		for (int j = 0; j < quarantinedRooms.size(); j++) {
			if (this->elems[i].getRoom().compare(quarantinedRooms[j]) == 0) {
				std::string newRoom = "Q" + this->elems[i].getRoom();
				this->elems[i].setRoom(newRoom);
				this->elems[i].setQuarantined(true);
			}
		}
		if (this->elems[i].getInfected() == true) {
			std::string newRoom = "Q" + this->elems[i].getRoom();
			this->elems[i].setRoom(newRoom);
			this->elems[i].setQuarantined(true);
			quarantinedRooms.push_back(std::to_string(i));
		}
	}
}

std::vector<Patient> Repo::getPatients()
{
	return this->elems;
}
