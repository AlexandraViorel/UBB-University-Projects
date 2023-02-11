#include "sourceFilesRepo.h"
#include <fstream>
#include <sstream>

void SourceFilesRepo::loadFile()
{
	std::ifstream f("files.txt");
	std::string line;
	std::string name, status, creator, reviewer;
	while (std::getline(f, line)) {
		std::istringstream s(line);
		std::getline(s, name, ';');
		std::getline(s, status, ';');
		std::getline(s, creator, ';');
		std::getline(s, reviewer, ';');
		this->addSourceFile(SourceFile{ name, status, creator, reviewer });
	}
	f.close();
}

SourceFilesRepo::SourceFilesRepo()
{
	this->loadFile();
}

void SourceFilesRepo::addSourceFile(SourceFile f)
{
	this->sourceFiles.push_back(f);
}

void SourceFilesRepo::updateSourceFile(std::string name, std::string newStatus, std::string newReviewer)
{
	for (int i = 0; i < this->sourceFiles.size(); i++) {
		if (this->sourceFiles[i].getName() == name) {
			SourceFile newFile{ name, newStatus, this->sourceFiles[i].getCreator(), newReviewer};
			this->sourceFiles.at(i) = newFile;
			return;
		}
	}
}

void SourceFilesRepo::sort()
{
	bool ok = false;
	do {
		ok = true;
		for (int i = 1; i < this->sourceFiles.size(); i++) {
			if (this->sourceFiles[i].getName() < this->sourceFiles[i - 1].getName()) {
				std::swap(this->sourceFiles[i], this->sourceFiles[i - 1]);
				ok = false;
			}
		}
	} while (!ok);
}

std::vector<SourceFile> SourceFilesRepo::getFiles()
{
	return this->sourceFiles;
}

std::string SourceFilesRepo::getFileCreator(std::string name)
{
	for (int i = 0; i < this->sourceFiles.size(); i++) {
		if (this->sourceFiles[i].getName() == name) {
			return this->sourceFiles[i].getCreator();
		}
	}
	return "";
}
