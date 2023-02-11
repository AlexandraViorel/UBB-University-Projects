#pragma once
#include "userRepository.h"

class CSVUserRepository : public UserRepository {
public:
	/// <summary>
	/// Constructor for CSVUserRepository
	/// </summary>
	/// <param name="CSVfileName">: the given CSV file name</param>
	CSVUserRepository(std::string CSVfileName);

	/// <summary>
	/// This function adds a dog to the adopting list.
	/// </summary>
	/// <param name="dog">: the dog to be added</param>
	void addDogUserRepo(Dog dog) override;

	//Dog findDogUserRepo(std::string name) override;

	/// <summary>
	/// This function gets the adopting list.
	/// </summary>
	/// <returns>: the adopting list</returns>
	std::vector<Dog> getAdoptingList() override;

	/// <summary>
	/// This function gets the CSV file name.
	/// </summary>
	/// <returns> the CSV file name</returns>
	std::string getFileName() override;

	/// <summary>
	/// This function writes the adopting list into the given file.
	/// </summary>
	void writeToFile() override;

	/// Destructor.
	~CSVUserRepository();
};