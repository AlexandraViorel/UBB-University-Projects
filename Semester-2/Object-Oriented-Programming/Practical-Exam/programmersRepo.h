#pragma once
#include <vector>
#include "programmer.h"

class ProgrammerRepo {
private:
	std::vector<Programmer> programmers;
	void loadFile();

public:
	ProgrammerRepo();

	void addProgrammer(Programmer p);

	void updateProgrammer(std::string name);

	int getProgRevised(std::string n);

	int getProgTotal(std::string n);

	std::vector<Programmer> getProgrammers();

};