#pragma once
#include <string>
#include <vector>
#include <iostream>

class Writer {
private:
	std::string name;
	std::string expertise;

public:
	Writer();
	Writer(std::string n, std::string e);
	std::string getName() const;
	std::string getExpertise() const;

	//friend std::istream& operator>>(std::istream& is, Writer& w);
};