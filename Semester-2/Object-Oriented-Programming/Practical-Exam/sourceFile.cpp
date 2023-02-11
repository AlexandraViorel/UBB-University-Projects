#include "sourceFile.h"

SourceFile::SourceFile(std::string n, std::string s, std::string c, std::string r) : name{ n }, status{ s }, creator{ c }, reviewer{ r }
{
}

std::string SourceFile::getName()
{
	return this->name;
}

std::string SourceFile::getStatus()
{
	return this->status;
}

std::string SourceFile::getCreator()
{
	return this->creator;
}

std::string SourceFile::getReviewer()
{
	return this->reviewer;
}
