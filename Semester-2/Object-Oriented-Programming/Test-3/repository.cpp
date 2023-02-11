#include "repository.h"
#include <fstream>

Repository::Repository(std::string f)
{
	this->fileName = f;
}

void Repository::loadFromFile()
{
	if (!fileName.empty())
	{
		Equation fileEq;
		std::ifstream fileIn(fileName);
		while (fileIn >> fileEq)
		{
			this->equs.push_back(fileEq);
		}
		fileIn.close();
	}
}

void Repository::addEq(Equation e)
{
	this->equs.push_back(e);
}

std::vector<Equation> Repository::getAll()
{
	return this->equs;
}
