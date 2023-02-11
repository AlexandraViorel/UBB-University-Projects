#pragma once
#include <string>

class Patient {
private:
	std::string name;
	int age;
	bool infected;
	std::string room;
	bool quarantined;
public:
	Patient(std::string _name, int _age, bool _infected, std::string _room, bool _quarantined);
	std::string getName() const;
	int getAge() const;
	bool getQuarantined() const;
	bool getInfected() const;
	std::string getRoom() const;
	
	void setRoom(std::string newRoom);
	void setQuarantined(bool x);

	std::string toStr() const;
};
