#pragma once
#include "repository.h"

class Service {
private:
	Repository& repo;

public:
	/// <summary>
	/// Constructor for the administrator service.
	/// </summary>
	/// <param name="repo">: the repository</param>
	Service(Repository& repo);

	/// <summary>
	/// This function adds a dog to the repository. If a dog with the same name exists, it throws
	/// an exception.
	/// </summary>
	/// <param name="name">: the name of the dog to be added</param>
	/// <param name="breed">: the breed of the dog to be added</param>
	/// <param name="age">: the age of the dog to be added</param>
	/// <param name="photoLink">: the photography link of the dog to be added</param>
	void addDogServ(std::string name, std::string breed, int age, std::string photoLink);

	/// <summary>
	/// This function removes a dog from the repository. If a dog with the given name does not exist,
	/// it throws an exception.
	/// </summary>
	/// <param name="name">: the name of the dog to be removed</param>
	void removeDogServ(std::string name);

	/// <summary>
	/// This function updates a dog from the repository. If a dog with the given name does not exist,
	/// it throws an exception.
	/// </summary>
	/// <param name="name">: the name of the dog to be updated</param>
	/// <param name="newBreed">: the new breed</param>
	/// <param name="newAge">: the new age</param>
	/// <param name="newPhotoLink">: the new photography link</param>
	void updateDogServ(std::string name, std::string newBreed, int newAge, std::string newPhotoLink);

	/// <summary>
	/// This function gets the list of dogs.
	/// </summary>
	/// <returns> the list of dogs</returns>
	std::vector<Dog> getDogsList();

	/// Destructor.
	~Service();
};