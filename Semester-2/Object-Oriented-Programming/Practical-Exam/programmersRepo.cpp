#include "programmersRepo.h"
#include <fstream>
#include <sstream>

void ProgrammerRepo::loadFile()
{
	std::ifstream f("programmers.txt");
	std::string line;
	std::string name, revisedFilesStr, totalFilesStr;
	while (std::getline(f, line)) {
		std::istringstream s(line);
		std::getline(s, name, ';');
		std::getline(s, revisedFilesStr, ';');
		std::getline(s, totalFilesStr, ';');
		this->addProgrammer(Programmer{ name, std::stoi(revisedFilesStr), std::stoi(totalFilesStr) });
	}
	f.close();
}

ProgrammerRepo::ProgrammerRepo()
{
	this->loadFile();
}

void ProgrammerRepo::addProgrammer(Programmer p)
{
	this->programmers.push_back(p);
}

void ProgrammerRepo::updateProgrammer(std::string name)
{
	for (int i = 0; i < this->programmers.size(); i++) {
		if (this->programmers[i].getName() == name) {
			int revised = this->programmers[i].getNoRevisedFiles();
			revised++;
			//int total = this->programmers[i].getTotalFilesToRevise();
			//total--;
			Programmer p{ name, revised, this->programmers[i].getTotalFilesToRevise() };
			this->programmers.at(i) = p;
			return;
		}
	}
}

int ProgrammerRepo::getProgRevised(std::string n)
{
	for (int i = 0; i < this->programmers.size(); i++) {
		if (this->programmers[i].getName() == n) {
			return this->programmers[i].getNoRevisedFiles();
		}
	}
	return -1;
}

int ProgrammerRepo::getProgTotal(std::string n)
{
	for (int i = 0; i < this->programmers.size(); i++) {
		if (this->programmers[i].getName() == n) {
			return this->programmers[i].getTotalFilesToRevise();
		}
	}
	return -1;
}

std::vector<Programmer> ProgrammerRepo::getProgrammers()
{
	return this->programmers;
}
