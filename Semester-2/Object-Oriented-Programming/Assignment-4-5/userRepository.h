#pragma once
#include "domain.h"
#include <vector>
#include <string>


class UserRepository {
protected:
	std::vector<Dog> adoptingList;
	std::string fileName;

public:
	/// <summary>
	/// Constructor for the user repositoy.
	/// </summary>
	UserRepository();

	/// <summary>
	/// This function adds a dog to the adopting list.
	/// </summary>
	/// <param name="dog">: the dog to be added</param>
	virtual void addDogUserRepo(Dog dog) = 0;

	/// <summary>
	/// This function gets the adopting list.
	/// </summary>
	/// <returns> the adopting list</returns>
	virtual std::vector<Dog> getAdoptingList() = 0;

	/// <summary>
	/// This function gets the file name.
	/// </summary>
	/// <returns> the file name</returns>
	virtual std::string getFileName() = 0;

	/// <summary>
	/// This function writes the dogs from the adopting list to the file.
	/// </summary>
	virtual void writeToFile() = 0;

	/// Destructor.
	~UserRepository();
};