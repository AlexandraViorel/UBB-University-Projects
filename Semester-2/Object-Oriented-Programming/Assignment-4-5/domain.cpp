#include "domain.h"
#include <vector>
#include <sstream>

Dog::Dog()
	: name{ "" }, breed{ "" }, age{ 0 }, photoLink{ "" }
{
}

Dog::Dog(const std::string& _name, const std::string& _breed, const int& _age, const std::string& _photoLink)
	: name{ _name }, breed{ _breed }, age{ _age }, photoLink{ _photoLink }
{
}

Dog::Dog(const Dog& dog)
{
	this->name = dog.name;
	this->breed = dog.breed;
	this->age = dog.age;
	this->photoLink = dog.photoLink;
}

std::string Dog::getBreed() const
{
	return this->breed;
}

std::string Dog::getName() const
{
	return this->name;
}

int Dog::getAge() const
{
	return this->age;
}

std::string Dog::getPhotoLink() const
{
	return this->photoLink;
}

void Dog::setBreed(std::string _breed)
{
	this->breed = _breed;
}

void Dog::setName(std::string _name)
{
	this->name = _name;
}

void Dog::setAge(int _age)
{
	this->age = _age;
}

void Dog::setPhotoLink(std::string _photoLink)
{
	this->photoLink = _photoLink;
}

std::string Dog::toString() const
{
	auto ageStr = std::to_string(this->age);
	return "Name: " + this->name + " | Breed: " + this->breed + " | Age: " + ageStr + " | Photo link: " + this->photoLink;

}

Dog::~Dog() = default;

std::vector<std::string> tokenize(const std::string & str, char delimiter)
{
	std::vector<std::string> result;
	std::stringstream ss(str);
	std::string token;
	while (getline(ss, token, delimiter))
	{
		result.push_back(token);
	}
	return result;
}

Dog& Dog::operator=(const Dog & dog)
{
	if (this == &dog)
	{
		return *this;
	}

	this->name = dog.name;
	this->breed = dog.breed;
	this->age = dog.age;
	this->photoLink = dog.photoLink;

	return *this;
}

bool Dog::operator==(const Dog & checkDog) const
{
	return this->name == checkDog.name;
}

std::ostream& operator<<(std::ostream & os, const Dog & dog)
{
	os << dog.getName() << ",";
	os << dog.getBreed() << ",";
	os << dog.getAge() << ",";
	os << dog.getPhotoLink();

	return os;
}

std::istream& operator>>(std::istream & reader, Dog & dog)
{
	std::string line;
	std::getline(reader, line);
	if (line.empty())
	{
		return reader;
	}
	std::vector<std::string> tokens;
	tokens = tokenize(line, ',');
	dog.name = tokens[0];
	dog.breed = tokens[1];
	dog.age = std::stoi(tokens[2]);
	dog.photoLink = tokens[3];
	return reader;
}

