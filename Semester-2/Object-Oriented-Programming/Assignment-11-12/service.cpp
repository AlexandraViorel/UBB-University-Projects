#include "service.h"
#include "errors.h"

Service::Service(Repository& repo) : repo{ repo } {}

void Service::addDogServ(std::string name, std::string breed, int age, std::string photoLink)
{
	Dog d = Dog(name, breed, age, photoLink);
	try
	{
		this->repo.addDogRepo(d);
	}
	catch (RepoError err)
	{
		throw err;
	}
}

void Service::removeDogServ(std::string name)
{
	try
	{
		this->repo.deleteDogRepo(name);
	}
	catch (RepoError err)
	{
		throw err;
	}
}

void Service::updateDogServ(std::string name, std::string newBreed, int newAge, std::string newPhotoLink)
{
	Dog newDog = Dog(name, newBreed, newAge, newPhotoLink);
	try
	{
		this->repo.updateDogRepo(name, newDog);
	}
	catch (RepoError err)
	{
		throw err;
	}
}

std::vector<Dog> Service::getDogsList()
{
	return this->repo.getDogsList();
}

std::vector<std::string> Service::getAllBreeds()
{
	std::vector<std::string> breeds;
	std::vector<Dog> dogs = this->repo.getDogsList();

	for (Dog d : dogs) {
		if (std::find(breeds.begin(), breeds.end(), d.getBreed()) == breeds.end()) {
			breeds.push_back(d.getBreed());
		}
	}

	return breeds;
}

int Service::getNbOfDogsWithGivenBreed(std::string breed)
{
	int count = 0;
	std::vector<Dog> dogs = this->repo.getDogsList();
	for (Dog d : dogs) {
		if (d.getBreed() == breed) {
			count++;
		}
	}
	return count;
}

Service::~Service() = default;