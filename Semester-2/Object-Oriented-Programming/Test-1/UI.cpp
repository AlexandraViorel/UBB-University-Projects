#include "UI.h"
#include <iostream>
#include <algorithm>

UI::UI(Service* serv)
{
	this->serv = serv;
}

void UI::printMenu()
{
	std::cout << "1. Remove patient\n";
	std::cout << "2. Show all patients\n";
	std::cout << "3. Quarantine patients\n";
	std::cout << "0. EXIT\n";
}

void UI::removeP()
{
	std::string name;
	std::cout << "Please input the name of the patient you want to remove: ";
	std::cin >> name;
	bool worked = this->serv->removePatientServ(name);
	if (worked == true) {
		std::cout << "Patient removed successfully !\n";
	}
	else {
		std::cout << "Patient cannot be removed !\n";
	}
}

bool comparator(Patient p1, Patient p2) {
	return p1.getAge() > p2.getAge();
}

void UI::printPatients()
{
	std::vector<Patient> v = this->serv->getAllPatients();
	std::sort(v.begin(), v.end(), comparator);
	for (int i = 0; i < v.size(); i++) {
		std::cout << v[i].toStr();
	}
}

void UI::quarantinePatients()
{
	this->serv->quarantinePatients();
	printPatients();
}

void UI::run()
{
	while (true) {
		int option;
		printMenu();
		std::cout << "Please input your option: ";
		std::cin >> option;
		if (option == 0) {
			return;
		}
		else if (option == 1) {
			removeP();
		}
		else if (option == 2) {
			printPatients();
		}
		else if (option == 3) {
			quarantinePatients();
		}
	}
}
