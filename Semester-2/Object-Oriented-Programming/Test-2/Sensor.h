#pragma once
#include <string>
#include <vector>

class Sensor {
protected:
	std::string producer;
	std::vector<double> recordings;
public:
	Sensor(std::string p, std::vector<double> v);
	std::string getProducer();
	virtual bool sendAlert() = 0;
	virtual double getPrice() = 0;
	virtual std::string toString();
};

class TemperatureSensor : public Sensor {
private:
	double diameter;
	double length;
public:
	TemperatureSensor(std::string p, std::vector<double> v, double d, double l);
	bool sendAlert() override;
	double getPrice() override;
	std::string toString() override;
};

class HumiditySensor : public Sensor {
public:
	HumiditySensor(std::string p, std::vector<double> v);
	bool sendAlert() override;
	double getPrice() override;
	std::string toString() override;
};

class SmokeSensor : public Sensor {
public:
	SmokeSensor(std::string p, std::vector<double> v);
	bool sendAlert() override;
	double getPrice() override;
	std::string toString() override;
};