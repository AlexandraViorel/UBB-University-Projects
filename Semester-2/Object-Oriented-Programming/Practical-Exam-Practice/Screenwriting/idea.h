#pragma once
#include <string>
#include <iostream>
#include <vector>

class Idea {
private:
	std::string description;
	std::string status;
	std::string creator;
	int act;

public:
	Idea();
	Idea(std::string d, std::string s, std::string c, int a);
	std::string getDescription() const;
	std::string getStatus() const;
	std::string getCreator() const;
	int getAct() const;

	void setStatus(std::string st);

	//friend std::istream& operator>>(std::istream& is, Idea& idea);
};