#include "Domain.h"

Patient::Patient(std::string _name, int _age, bool _infected, std::string _room, bool _quarantined)
{
	this->name = _name;
	this->age = _age;
	this->infected = _infected;
	this->room = _room;
	this->quarantined = _quarantined;
}

std::string Patient::getName() const
{
	return this->name;
}

int Patient::getAge() const
{
	return this->age;
}

bool Patient::getQuarantined() const
{
	return this->quarantined;
}

bool Patient::getInfected() const
{
	return this->infected;
}

std::string Patient::getRoom() const
{
	return this->room;
}

void Patient::setRoom(std::string newRoom)
{
	this->room = newRoom;
}

void Patient::setQuarantined(bool x)
{
	this->quarantined = x;
}

std::string boolToStr(bool x) {
	if (x == true) {
		return "true";
	}
	return "false";
}

std::string Patient::toStr() const
{
	std::string ageStr = std::to_string(this->age);
	std::string infectedStr = boolToStr(this->infected);
	std::string quarantinedStr = boolToStr(this->quarantined);
	return this->name + " | " + ageStr + " | " + infectedStr + " | " + this->room + " | " + quarantinedStr + "\n";
}
