#include "repository.h"
#include "errors.h"
#include <fstream>

void Repository::loadEntitiesFromFile()
{
	if (!fileName.empty())
	{
		Dog fileDog;
		std::ifstream fileIn(fileName);
		while (fileIn >> fileDog)
		{
			if (std::find(administratorList.begin(), administratorList.end(), fileDog) == administratorList.end())
			{
				administratorList.push_back(fileDog);
			}
		}
		fileIn.close();
	}
}

void Repository::writeEntitiesToFile()
{
	if (!fileName.empty())
	{
		std::ofstream fileOut(fileName);
		for (auto dog : administratorList)
		{
			fileOut << dog << "\n";
		}
		fileOut.close();
	}
}

Repository::Repository(std::string fileName)
{
	this->fileName = fileName;
}

Dog Repository::findDogRepo(std::string name)
{
	for (auto i : administratorList)
	{
		if (i.getName() == name)
		{
			return i;
		}
	}
	throw ValueError("Dog not found !");
}

void Repository::addDogRepo(Dog dog)
{
	try
	{
		Dog d = findDogRepo(dog.getName());
		throw RepoError("This dog already exists !");
	}
	catch (ValueError)
	{
		this->administratorList.push_back(dog);
		this->writeEntitiesToFile();
	}
}

bool nameEqual(std::string s1, std::string s2)
{
	if (s1 == s2)
	{
		return true;
	}
	return false;
}

void Repository::deleteDogRepo(std::string name)
{
	auto it = std::remove_if(administratorList.begin(), administratorList.end(), [name](Dog d) { return (d.getName() == name); });
	if (it == administratorList.end())
	{
		throw RepoError("Dog does not exist !");
	}
	administratorList.pop_back();
	this->writeEntitiesToFile();
}

void Repository::updateDogRepo(std::string name, Dog newDog)
{
	int k = 0;
	for (Dog i : administratorList)
	{
		if (i.getName() == name)
		{
			administratorList.at(k) = newDog;
			return;
		}
		k++;
	}
	throw RepoError("Dog does not exist !");
}

std::vector<Dog> Repository::getDogsList() const
{
	return this->administratorList;
}

Repository::~Repository() = default;