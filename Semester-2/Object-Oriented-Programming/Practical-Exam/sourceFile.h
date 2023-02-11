#pragma once
#include <string>

class SourceFile {
private:
	std::string name;
	std::string status;
	std::string creator;
	std::string reviewer;

public:
	SourceFile(std::string n, std::string s, std::string c, std::string r);

	std::string getName();
	std::string getStatus();
	std::string getCreator();
	std::string getReviewer();
};