#include "CSVUserRepository.h"
#include <fstream>

CSVUserRepository::CSVUserRepository(std::string CSVfileName)
{
	this->fileName = CSVfileName;
}

void CSVUserRepository::addDogUserRepo(Dog dog)
{
	this->adoptingList.push_back(dog);
	this->writeToFile();
}

std::vector<Dog> CSVUserRepository::getAdoptingList()
{
	return this->adoptingList;
}

std::string CSVUserRepository::getFileName()
{
	return this->fileName;
}

void CSVUserRepository::writeToFile()
{
	std::ofstream fileOut(fileName);
	if (!adoptingList.empty())
	{
		for (auto dog : adoptingList)
		{
			fileOut << dog << "\n";
		}
	}
	fileOut.close();
}

CSVUserRepository::~CSVUserRepository() = default;
