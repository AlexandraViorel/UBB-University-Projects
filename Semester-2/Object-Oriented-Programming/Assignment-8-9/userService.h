#pragma once
#include "userRepository.h"

class UserService {
private:
	UserRepository* userRepo;

public:
	/// <summary>
	/// Constructor for the user service.
	/// </summary>
	UserService();

	/// <summary>
	/// Constructor for the user service.
	/// </summary>
	/// <param name="userRepo">: the user repository</param>
	UserService(UserRepository* userRepo);

	/// <summary>
	/// This function adds a dog to the adopting list.
	/// </summary>
	/// <param name="name">: the name of the dog to be added</param>
	/// <param name="breed">: the breed of the dog to be added</param>
	/// <param name="age">: the age of the dog to be added</param>
	/// <param name="photoLink">: the photography link of the dog to be added</param>
	void addDogUserServ(std::string name, std::string breed, int age, std::string photoLink);

	/// <summary>
	/// This function gets the adopting list.
	/// </summary>
	/// <returns> the adopting list</returns>
	std::vector<Dog> getAdoptingList();

	/// <summary>
	/// This function gets the file name.
	/// </summary>
	/// <returns></returns>
	std::string getFileName();

	/// <summary>
	/// This function chooses the type of the file where the adopting list will be stored.
	/// </summary>
	/// <param name="fileType">; the given file type</param>
	void chooseRepositoryType(int fileType);

	/// Destructor.
	~UserService();
};