#include "UI.h"
#include "errors.h"

void UI::handleAdd()
{
	std::string name, breed, photoLink;
	int age;

	std::cout << "Please input the name: ";
	std::getline(std::cin, name);

	std::cout << "Please input the breed: ";
	std::getline(std::cin, breed);

	std::cout << "Please input the age: ";
	std::cin >> age;
	std::cin.get();
	if (std::cin.fail())
	{
		std::cout << "Invalid input! \n";
		std::cin.clear();
		std::cin.ignore(256, '\n');
		return;
	}

	std::cout << "Please input the photography link: ";
	std::getline(std::cin, photoLink);

	try
	{
		this->adminService.addDogServ(name, breed, age, photoLink);
		std::cout << "Dog added successfully !\n";
	}
	catch (RepoError err)
	{
		std::cout << err.what() << '\n';
	}
}

void UI::handleRemove()
{
	std::string name;

	std::cout << "Please input the name: ";
	std::getline(std::cin, name);

	try
	{
		this->adminService.removeDogServ(name);
		std::cout << "Dog removed successfully !\n";
	}
	catch (RepoError err)
	{
		std::cout << err.what() << '\n';
	}
}

void UI::handleUpdate()
{
	std::string name, newBreed, newPhotoLink;
	int newAge;

	std::cout << "Please input the name of the dog you want to update: ";
	std::getline(std::cin, name);

	std::cout << "Please input the new breed: ";
	std::getline(std::cin, newBreed);

	std::cout << "Please input the new age: ";
	std::cin >> newAge;
	std::cin.get();
	if (std::cin.fail())
	{
		std::cout << "Invalid input!\n";
		std::cin.clear();
		std::cin.ignore(256, '\n');
		return;
	}

	std::cout << "Please input the new photography link: ";
	std::getline(std::cin, newPhotoLink);

	try
	{
		this->adminService.updateDogServ(name, newBreed, newAge, newPhotoLink);
		std::cout << "Dog updated successfully !\n";
	}
	catch (RepoError err)
	{
		std::cout << err.what() << '\n';
	}
}

void UI::printDogs()
{
	std::vector<Dog> arr = this->adminService.getDogsList();
	for (auto i : arr)
	{
		std::cout << i << '\n';
	}
}

void UI::printAdoptingList()
{
	std::vector<Dog> arr = this->userService.getAdoptingList();
	for (auto i : arr)
	{
		std::cout << i << '\n';
	}
}

void UI::handleAdoptAll()
{
	std::vector<Dog> arr = this->adminService.getDogsList();
	for (auto i : arr)
	{
		std::cout << i << '\n';
		std::string command = std::string("start ").append(i.getPhotoLink());
		system(command.c_str());
		int addToAdoptionList;
		std::cout << "Add to adoption list? (1.Yes/2.No):\n";
		std::cin >> addToAdoptionList;
		std::cin.get();
		if (addToAdoptionList == 1)
		{
			try
			{
				this->userService.addDogUserServ(i.getName(), i.getBreed(), i.getAge(), i.getPhotoLink());
			}
			catch (RepoError err)
			{
				std::cout << err.what() << '\n';
			}
		}
		int next;
		std::cout << "Continue? (1.Yes/2.No):\n";
		std::cin >> next;
		std::cin.get();
		if (next != 1)
		{
			break;
		}
	}
}

void UI::handleAdoptFiltered()
{
	std::string breed;
	int age;

	std::cout << "Please input the breed: ";
	std::cin >> breed;

	std::cout << "Please input the age: ";
	std::cin >> age;

	std::vector<Dog> arr = this->adminService.getDogsList();
	for (auto i : arr)
	{
		if (breed == "-1" || (breed == i.getBreed() && age > i.getAge()))
		{
			std::cout << i << '\n';
			std::string command = std::string("start ").append(i.getPhotoLink());
			system(command.c_str());
			int addToAdoptionList;
			std::cout << "Add to adoption list? (1.Yes/2.No):\n";
			std::cin >> addToAdoptionList;
			std::cin.get();
			if (addToAdoptionList == 1)
			{
				try
				{
					this->userService.addDogUserServ(i.getName(), i.getBreed(), i.getAge(), i.getPhotoLink());
				}
				catch (RepoError err)
				{
					std::cout << err.what() << '\n';
				}
			}
			int next;
			std::cout << "Continue? (1.Yes/2.No):\n";
			std::cin >> next;
			std::cin.get();
			if (next != 1)
			{
				break;
			}
		}
	}
}

void UI::openFile()
{
	std::string command = std::string("start ").append(this->userService.getFileName());
	system(command.c_str());
}

void UI::displayAdminMenu()
{
	std::cout << "1. Add dog \n";
	std::cout << "2. Remove dog \n";
	std::cout << "3. Update dog \n";
	std::cout << "4. Display dogs \n";
	std::cout << "5. Exit \n";
	std::cout << "Please choose an option: ";
}

void UI::displayUserMenu()
{
	std::cout << "1. See all dogs \n";
	std::cout << "2. See dogs of a given breed and age (if breed=-1, all dogs) \n";
	std::cout << "3. Display adopting list \n";
	std::cout << "4. Display adopting list in file\n";
	std::cout << "5. Exit\n";
	std::cout << "Please choose an option: ";
}

UI::UI(Service& adminService, UserService& userService) : adminService{ adminService }, userService{ userService } {}

void UI::run()
{
	int option;
	int userFile = 0;
	std::cout << "1. Administrator mode\n";
	std::cout << "2. User mode\n";
	std::cout << "3. Exit\n\n";
	std::cout << "Please choose an option: ";
	std::cin >> option;
	if (option == 1)
	{
		while (true)
		{
			displayAdminMenu();
			std::cin >> option;
			std::cin.get();
			if (std::cin.fail())
			{
				std::cout << "Invalid input!\n";
				std::cin.clear();
				std::cin.ignore(256, '\n');
				return;
			}
			if (option == 1)
			{
				this->handleAdd();
			}
			else if (option == 2)
			{
				this->handleRemove();
			}
			else if (option == 3)
			{
				this->handleUpdate();
			}
			else if (option == 4)
			{
				this->printDogs();
			}
			else if (option == 5)
			{
				return;
			}
			else
			{
				std::cout << "Invalid option! Try again!\n";
			}
		}
	}
	else if (option == 2)
	{
		if (userFile == 0)
		{
			int fileOption;
			std::cout << "File types:\n1.CSV\n2.HTML\n";
			std::cout << "Please choose the file type: ";
			std::cin >> fileOption;
			if (std::cin.fail())
			{
				std::cout << "Invalid input!\n";
				std::cin.clear();
				std::cin.ignore(256, '\n');
				return;
			}
			else if (fileOption == 1 || fileOption == 2)
			{
				this->userService.chooseRepositoryType(fileOption);
				userFile = 1;
			}
		}
		while (true)
		{
			displayUserMenu();
			std::cin >> option;
			std::cin.get();
			if (std::cin.fail())
			{
				std::cout << "Invalid input!\n";
				std::cin.clear();
				std::cin.ignore(256, '\n');
				return;
			}
			if (option == 1)
			{
				this->handleAdoptAll();
			}
			else if (option == 2)
			{
				this->handleAdoptFiltered();
			}
			else if (option == 3)
			{
				this->printAdoptingList();
			}
			else if (option == 4)
			{
				this->openFile();
			}
			else if (option == 5)
			{
				return;
			}
			else
			{
				std::cout << "Invalid option! Try again!\n";
			}
		}
	}
	else
	{
		return;
	}
}

UI::~UI() = default;
