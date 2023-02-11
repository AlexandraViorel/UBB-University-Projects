#pragma once
#include "domain.h"
#include <vector>

class Repository {
private:
	std::vector<Dog> administratorList;
	std::string fileName;

public:
	/// <summary>
	/// This function loads the dogs from the given file into the repository.
	/// </summary>
	void loadEntitiesFromFile();

	/// <summary>
	/// This function writes the dogs from the repository into the given file.
	/// </summary>
	void writeEntitiesToFile();

	/// <summary>
	/// This is the constructor for the repository.
	/// </summary>
	/// <param name="fileName">: the given file from where we read dogs and where we write dogs</param>
	Repository(std::string fileName);

	/// <summary>
	/// This function finds a dog with the given name.
	/// </summary>
	/// <param name="name">: the given name of the dog</param>
	/// <returns>the dog if it finds it, else throws an exception</returns>
	Dog findDogRepo(std::string name);

	/// <summary>
	/// This function adds a dog to the repository. It throws an exception if the dog already exists.
	/// </summary>
	/// <param name="dog">: the dog to be added</param>
	void addDogRepo(Dog dog);

	/// <summary>
	/// This function deletes a dog from the repository. It throws an exception if the dog does not
	/// exist.
	/// </summary>
	/// <param name="name">: the name of the dog to be deleted</param>
	void deleteDogRepo(std::string name);

	/// <summary>
	/// This function updates the informations about the dog with a given name. It throws an exception
	/// if the dog does not exist.
	/// </summary>
	/// <param name="name">: the name of the dog to be updated</param>
	/// <param name="newDog">: the new dog</param>
	void updateDogRepo(std::string name, Dog newDog);

	/// <summary>
	/// This function gets the dogs list from the repository.
	/// </summary>
	/// <returns>the dogs list</returns>
	std::vector<Dog> getDogsList() const;

	/// Destructor.
	~Repository();
};