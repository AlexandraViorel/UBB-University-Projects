#pragma once

#include <string>
#include <iostream>

class Dog {
private:
	std::string name;
	std::string breed;
	int age;
	std::string photoLink;

public:
	/// <summary>
	/// Constructor for the dog
	/// </summary>
	Dog();

	/// <summary>
	/// Constructor for the dog
	/// </summary>
	/// <param name=""></param>
	/// <param name=""></param>
	/// <param name=""></param>
	/// <param name=""></param>
	Dog(const std::string&, const std::string&, const int&, const std::string&);

	/// <summary>
	/// Constructor for the dog
	/// </summary>
	/// <param name="dog"></param>
	Dog(const Dog& dog);

	/// <summary>
	/// Breed getter
	/// </summary>
	/// <returns>: the breed</returns>
	std::string getBreed() const;

	/// <summary>
	/// Name getter
	/// </summary>
	/// <returns>: the name</returns>
	std::string getName() const;

	/// <summary>
	/// Age getter
	/// </summary>
	/// <returns>: the age</returns>
	int getAge() const;

	/// <summary>
	/// Photography link getter
	/// </summary>
	/// <returns>: the photography link</returns>
	std::string getPhotoLink() const;

	/// <summary>
	/// Breed setter
	/// </summary>
	/// <param name="_breed"></param>
	void setBreed(std::string _breed);

	/// <summary>
	/// Name setter
	/// </summary>
	/// <param name="_name"></param>
	void setName(std::string _name);

	/// <summary>
	/// Age setter
	/// </summary>
	/// <param name="_age"></param>
	void setAge(int _age);

	/// <summary>
	/// Photography link setter
	/// </summary>
	/// <param name="_photoLink"></param>
	void setPhotoLink(std::string _photoLink);

	std::string toString() const;

	/// Dog destructor
	~Dog();

	Dog& operator=(const Dog& dog);

	bool operator==(const Dog& checkDog) const;

	friend std::ostream& operator<<(std::ostream& os, const Dog& dog);

	friend std::istream& operator>>(std::istream& reader, Dog& dog);
};