#include "Service.h"
#include <fstream>
#include <algorithm>

Service::Service(bool WiFi)
{
	this->hasWiFi = WiFi;
}

void Service::initialize()
{
	std::vector<double> v1;
	v1.push_back(9);
	v1.push_back(50);
	TemperatureSensor* s1 = new TemperatureSensor("producer1", v1, 10, 100);
	std::vector<double> v2;
	v2.push_back(9);
	v2.push_back(50);
	HumiditySensor* s2 = new HumiditySensor("producer2", v2);
	std::vector<double> v3;
	v3.push_back(9);
	v3.push_back(50);
	SmokeSensor* s3 = new SmokeSensor("producer3", v3);

	this->sensorsList.push_back(s1);
	this->sensorsList.push_back(s2);
	this->sensorsList.push_back(s3);
}

void Service::addSensor(Sensor* s)
{
	this->sensorsList.push_back(s);
}

std::vector<Sensor*> Service::getAllSensors()
{
	return this->sensorsList;
}

std::vector<Sensor*> Service::getAlertingSensors()
{
	std::vector<Sensor*> alertingSensors;
	for (auto sensor : this->sensorsList) {
		if (sensor->sendAlert() == true) {
			alertingSensors.push_back(sensor);
		}
	}
	return alertingSensors;
}

bool comparator(Sensor* s1, Sensor* s2) {
	if (s1->getProducer().compare(s2->getProducer()) < 0) {
		return true;
	}
	return false;
}

void Service::writeToFile(std::string filename)
{
	std::vector<Sensor*> vec = this->sensorsList;
	std::ofstream fileOut(filename);
	fileOut << this->getPrice() << "\n";
	if (this->hasWiFi == true) {
		fileOut << "has WiFi" << "\n";
	}
	else {
		fileOut << "no WiFi" << "\n";
	}
	std::sort(vec.begin(), vec.end(), comparator);
	for (auto sensor : vec) {
		fileOut << sensor->toString();
	}
}

double Service::getPrice()
{
	double pr = 19;
	if (this->hasWiFi == true) {
		pr += 20;
	}
	for (auto sensor : this->sensorsList) {
		pr += sensor->getPrice();
	}
	return pr;
}