#include "SetIterator.h"
#include "Set.h"
#include <exception>

SetIterator::SetIterator(const Set& m) : set(m)
{
	//this->index = 0;
	this->capacity = this->set.capacity;
	//while (this->index < this->capacity && (this->set.hashTable[this->index] == this->set.empty || this->set.hashTable[this->index] == this->set.deleted))
	//{
	//	this->index++;
	//}
	this->first();
}


void SetIterator::first() {
	this->index = 0;
	while (this->index < this->capacity && (this->set.hashTable[this->index] == this->set.empty || this->set.hashTable[this->index] == this->set.deleted))
	{
		this->index++;
	}
}


void SetIterator::next() {
	if (!valid())
	{
		throw std::exception();
		//return;
	}
	this->index++;
	while (valid() && (this->set.hashTable[this->index] == this->set.empty || this->set.hashTable[this->index] == this->set.deleted))
	{
		this->next();
	}
}


TElem SetIterator::getCurrent()
{
	if (valid())
	{
		return this->set.hashTable[this->index];
	}
	else 
	{
		throw std::exception();
	}

	//int i = 0;
	//while (i < this->length && (this->set.hashTable[i] == this->set.empty || this->set.hashTable[i] == this->set.deleted))
	//{
	//	i++;
	//}
}

bool SetIterator::valid() const 
{
	return this->index < this->capacity && this->index >= 0;
}



