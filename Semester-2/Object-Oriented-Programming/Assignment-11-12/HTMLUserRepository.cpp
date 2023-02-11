#include "HTMLUserRepository.h"
#include <fstream>

HTMLUserRepository::HTMLUserRepository(std::string HTMLfileName)
{
	this->fileName = HTMLfileName;
}

void HTMLUserRepository::addDogUserRepo(Dog dog)
{
	this->adoptingList.push_back(dog);
	this->writeToFile();
}

std::vector<Dog> HTMLUserRepository::getAdoptingList()
{
	return this->adoptingList;
}

std::string HTMLUserRepository::getFileName()
{
	return this->fileName;
}

void HTMLUserRepository::writeToFile()
{
	std::ofstream fileOut(fileName);
	fileOut << "<!DOCTYPE html>\n<html><head><title>Adopting list</title></head><body>\n";
	fileOut << "<table border=\"1\">\n";
	fileOut << "<tr><td>Name</td><td>Breed</td><td>Age</td><td>Photo link</td></tr>\n";
	for (Dog dog : adoptingList)
	{
		fileOut << "<tr><td>" << dog.getName() << "</td><td>" << dog.getBreed() << "</td><td>"
			<< std::to_string(dog.getAge()) << "</td>" << "<td><a href = \"" << dog.getPhotoLink()
			<< "\">" << dog.getPhotoLink() << "</a></td></tr>\n";
	}
	fileOut << "</table></body></html>";
	fileOut.close();
}

HTMLUserRepository::~HTMLUserRepository() = default;
