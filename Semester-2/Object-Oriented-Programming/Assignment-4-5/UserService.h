#pragma once
#include <string>
#include "Dog.h"
#include "UserRepository.h"
#include "DynamicArrayG.h"

class UserService
{
private:
	AdoptingRepository& repo;

public:
	UserService(AdoptingRepository& repo);

	void add(std::string name, std::string breed, int age, std::string photoLink);

	void remove(std::string name);

	std::vector<Dog> getAdoptingList();
};