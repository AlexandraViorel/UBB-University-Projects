#pragma once
#include "userRepository.h"

class HTMLUserRepository : public UserRepository {
public:
	/// <summary>
	/// Constructor for HTMLUserRepository.
	/// </summary>
	/// <param name="HTMLfileName">: the given HTML file name</param>
	HTMLUserRepository(std::string HTMLfileName);

	/// <summary>
	/// This function adds the given dog to the adopting list.
	/// </summary>
	/// <param name="dog">: the dog to be added</param>
	void addDogUserRepo(Dog dog) override;

	/// <summary>
	/// This function gets the adopting list.
	/// </summary>
	/// <returns>: the adopting list</returns>
	std::vector<Dog> getAdoptingList() override;

	/// <summary>
	/// This function gets the HTML file name.
	/// </summary>
	/// <returns> the HTML file name</returns>
	std::string getFileName() override;

	/// <summary>
	/// This function writes the adopting list into the given file.
	/// </summary>
	void writeToFile() override;

	/// Destructor.
	~HTMLUserRepository() override;
};