#pragma once
#include <string>

class Programmer {
private:
	std::string name;
	int noRevisedFiles;
	int totalFilesToRevise;

public:
	Programmer(std::string n, int r, int t);

	std::string getName();

	int getNoRevisedFiles();

	int getTotalFilesToRevise();

	void setRevisedFiles(int newRev);

	void setTotalFiles(int newTot);
};