#include "ui.h"
#include <iostream>

UI::UI(Service& s) : serv{s} {}

void UI::printMenu()
{
	std::cout << "1. Add sensor \n";
	std::cout << "2. List all \n";
	std::cout << "3. List alert \n";
	std::cout << "4. Save to file \n";
	std::cout << "0. Exit \n";
}

void UI::handleAdd()
{
	std::cout << "Please input the type: (1-temperature, 2-humidity, 3-smoke): ";
	int opt;
	std::cin >> opt;
	std::cout << "Please input the producer: ";
	std::string prod;
	std::cin >> prod;
	std::cout << "Please input how many recordings: ";
	int r;
	std::cin >> r;
	std::vector<double> v;
	for (int i = 0; i < r; i++) {
		std::cout << "Please input the recording: ";
		double rec;
		std::cin >> rec;
		v.push_back(rec);
	}
	if (opt == 1) {
		std::cout << "Please input the diameter: ";
		double dia;
		std::cin >> dia;
		std::cout << "Please input the length: ";
		double leng;
		std::cin >> leng;
		TemperatureSensor* s = new TemperatureSensor(prod, v, dia, leng);
		this->serv.addSensor(s);
	}
	else if (opt == 2) {
		HumiditySensor* s = new HumiditySensor(prod, v);
		this->serv.addSensor(s);
	}
	else {
		SmokeSensor* s = new SmokeSensor(prod, v);
		this->serv.addSensor(s);
	}

}

void UI::handleListAll()
{
	std::vector<Sensor*> vec = this->serv.getAllSensors();
	for (auto sensor : vec) {
		std::cout << sensor->toString();
	}
}

void UI::handleListAlert()
{
	std::vector<Sensor*> vec = this->serv.getAlertingSensors();
	for (auto sensor : vec) {
		std::cout << sensor->toString();
	}
}

void UI::run()
{
	this->serv.initialize();
	int option;
	while (true) {
		this->printMenu();
		std::cout << "Please input your option: ";
		std::cin >> option;
		if (option == 1) {
			this->handleAdd();
		}
		else if (option == 2) {
			this->handleListAll();
		}
		else if (option == 3) {
			this->handleListAlert();
		}
		else if (option == 4) {
			this->serv.writeToFile("sensors.txt");
		}
		else if (option == 0) {
			return;
		}
		else {
			std::cout << "Invalid option!";
		}
	}
}
