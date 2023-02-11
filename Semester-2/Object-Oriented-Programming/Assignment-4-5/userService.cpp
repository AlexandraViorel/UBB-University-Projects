#include "userService.h"
#include "errors.h"
#include "CSVUserRepository.h"
#include "HTMLUserRepository.h"

UserService::UserService()
{
}

UserService::UserService(UserRepository* userRepo)
{
	this->userRepo = userRepo;
}

void UserService::addDogUserServ(std::string name, std::string breed, int age, std::string photoLink)
{
	Dog d = Dog(name, breed, age, photoLink);
	try
	{
		this->userRepo->addDogUserRepo(d);
	}
	catch (RepoError err)
	{
		throw err;
	}
}

std::vector<Dog> UserService::getAdoptingList()
{
	return this->userRepo->getAdoptingList();
}

std::string UserService::getFileName()
{
	return this->userRepo->getFileName();
}

void UserService::chooseRepositoryType(int fileType)
{
	if (fileType == 1)
	{
		std::string file = R"(D:\\Faculty materials\\1st year\\2nd semester\\OOP\\C++ projects\\A9\\A9\\adoptionList.csv)";
		auto* repo = new CSVUserRepository{ file };
		this->userRepo = repo;
	}
	else if (fileType)
	{
		std::string file = R"(D:\\Faculty materials\\1st year\\2nd semester\\OOP\\C++ projects\\A9\\A9\\adoptionList.html)";
		auto* repo = new HTMLUserRepository{ file };
		this->userRepo = repo;
	}
}

UserService::~UserService() = default;