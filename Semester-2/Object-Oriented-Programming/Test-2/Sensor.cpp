#include "Sensor.h"

Sensor::Sensor(std::string p, std::vector<double> v)
{
    this->producer = p;
    this->recordings = v;
}

std::string Sensor::getProducer()
{
    return this->producer;
}

std::string Sensor::toString()
{
    return "";
}

TemperatureSensor::TemperatureSensor(std::string p, std::vector<double> v, double d, double l) : Sensor(p, v)
{
    this->diameter = d;
    this->length = l;
}

bool TemperatureSensor::sendAlert()
{
    int k = 0;
    for (auto i : this->recordings) {
        if (i < 10 || i > 35) {
            k++;
        }
    }
    if (k >= 2) return true;
    return false;
}

double TemperatureSensor::getPrice()
{
    if (this->diameter < 3 && this->length < 50) {
        return 17;
    }
    return 9;
}

std::string boolToString(bool x) {
    if (x == true) {
        return "true";
    }
    return "false";
}

std::string TemperatureSensor::toString()
{
    std::string s = "TEMPERATURE = Producer: " + this->producer + ", " + " Recordings: ";
    for (auto i : this->recordings) {
        s += std::to_string(i);
        s += " ";
    }
    s += " Diameter: ";
    s += std::to_string(this->diameter);
    s += ", Length: ";
    s += std::to_string(this->length);
    s += ", Price: ";
    s += std::to_string(this->getPrice());
    s += ", Alert: ";
    s += boolToString(this->sendAlert());
    s += "\n";
    return s;
}

HumiditySensor::HumiditySensor(std::string p, std::vector<double> v) : Sensor(p, v) {}

bool HumiditySensor::sendAlert()
{
    int k = 0;
    for (auto i : this->recordings) {
        if (i < 30 || i > 85) {
            k++;
        }
    }
    if (k >= 2) return true;
    return false;
}

double HumiditySensor::getPrice()
{
    return 4;
}

std::string HumiditySensor::toString()
{
    std::string s = "HUMIDITY = Producer: " + this->producer + ", " + " Recordings: ";
    for (auto i : this->recordings) {
        s += std::to_string(i);
        s += " ";
    }
    s += ", Price: ";
    s += std::to_string(this->getPrice());
    s += ", Alert: ";
    s += boolToString(this->sendAlert());
    s += "\n";
    return s;
}

SmokeSensor::SmokeSensor(std::string p, std::vector<double> v) : Sensor(p, v) {}

bool SmokeSensor::sendAlert()
{
    int k = 0;
    for (auto i : this->recordings) {
        if (i > 1600) {
            k++;
        }
    }
    if (k >= 1) return true;
    return false;
}

double SmokeSensor::getPrice()
{
    return 25;
}

std::string SmokeSensor::toString()
{
    std::string s = "SMOKE = Producer: " + this->producer + ", " + " Recordings: ";
    for (auto i : this->recordings) {
        s += std::to_string(i);
        s += " ";
    }
    s += ", Price: ";
    s += std::to_string(this->getPrice());
    s += ", Alert: ";
    s += boolToString(this->sendAlert());
    s += "\n";
    return s;
}
