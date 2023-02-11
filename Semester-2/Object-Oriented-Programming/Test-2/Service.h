#pragma once
#include "Sensor.h"

class Service {
private:
	bool hasWiFi;
	std::vector<Sensor*> sensorsList;
public:
	Service(bool WiFi);
	void initialize();
	void addSensor(Sensor* s);
	std::vector<Sensor*> getAllSensors();
	std::vector<Sensor*> getAlertingSensors();
	void writeToFile(std::string filename);
	double getPrice();
};