#include "MultiMapIterator.h"
#include "MultiMap.h"
#include <exception>


MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) 
{
	this->currentNode = this->col.head;
}

// Complexity: Theta(1)
TElem MultiMapIterator::getCurrent() const
{
	if (valid())
	{
		int key = this->currentNode->info.first;
		int value = this->currentNode->info.second;
		return std::make_pair(key, value);
	}
	else
	{
		throw exception();
	}
}

// Complexity: Theta(1)
bool MultiMapIterator::valid() const 
{
	if (this->currentNode != NULL) 
	{
		return true;
	}
	return false;
}

// Complexity: Theta(1)
void MultiMapIterator::next() 
{
	if (valid())
	{
		this->currentNode = this->currentNode->next;
	}
	else
	{
		throw exception();
	}
}

// Complexity: Theta(1)
void MultiMapIterator::first() 
{
	this->currentNode = this->col.head;
}

