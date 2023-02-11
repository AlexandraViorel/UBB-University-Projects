#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>
#include <vector>

using namespace std;

// Complexity: Theta(1)
MultiMap::MultiMap() 
{
	this->head = NULL;
	this->tail = NULL;
	this->length = 0;
}

// Complexity: O(1) because every element is added at the beginning 
void MultiMap::add(TKey c, TValue v) 
{
	if (this->head == NULL && this->tail == NULL)
	{
		node* newNode = new node;
		newNode->info = std::make_pair(c, v);
		newNode->previous = NULL;
		newNode->next = NULL;
		this->head = newNode;
		this->tail = newNode;
		this->length++;
	}
	else
	{
		node* newNode = new node;
		newNode->info = std::make_pair(c, v);
		newNode->previous = NULL;
		newNode->next = this->head;
		this->head->previous = newNode;
		this->head = newNode;
		this->length++;
	}	
}

// Complexity: O(length of the multi map)
// Best case: Theta(1) when the first element is removed
// Worst case: O(length of the multi map)
bool MultiMap::remove(TKey c, TValue v) 
{
	if (this->isEmpty())
	{
		return  false;
	}
	node* n = this->head;
	node* previous = NULL;

	for (n; n != NULL; previous = n, n = n->next)
	{
		if (n->info.first == c)
		{
			if (n->info.second == v)
			{
				if (previous == NULL)
				{
					this->head = n->next;
				}
				else
				{
					previous->next = n->next;
				}
				delete n;
				this->length--;
				return true;
			}
		}
	}
	return false;
}

// Complexity: Theta(length of the multi map)
vector<TValue> MultiMap::search(TKey c) const 
{
	vector<TValue> v = vector<TValue>();
	node* n = this->head;
	while (n != NULL)
	{
		if (n->info.first == c)
		{
			v.push_back(n->info.second);
		}
		n = n->next;
	}
	return v;
}

// Complexity: Theta(1)
int MultiMap::size() const 
{
	return this->length;
}

// Complexity: Theta(1)
bool MultiMap::isEmpty() const 
{
	if (this->head == NULL && this->tail == NULL)
	{
		return true;
	}
	return false;
}

// Complexity: Theta(1)
MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}

// Complexity : O(n)
int MultiMap::findTValue(vector<TValue> values, TValue v) const
{
	for (int i = 0; i < values.size(); i++)
	{
		if (values[i] == v)
		{
			return i;
		}
	}
	return -1;
}

// Complexity: Theta(length^2)
// Best case: Theta(1), when the MultiMap is empty
// Worst case: O(length^2)
TValue MultiMap::mostFrequent() const
{
	if (this->length == 0)
	{
		return NULL_TVALUE;
	}
	vector<TValue> values;
	vector<int> frequencies;
	node* current = this->head;
	while (current != NULL)
	{
		int pos = findTValue(values, current->info.second);
		if (pos == -1)
		{
			values.push_back(current->info.second);
			frequencies.push_back(0);
		}
		else
		{
			frequencies.at(pos) = frequencies[pos] + 1;
		}
		current = current->next;
	}

	int max = -1;
	int maxPos = 0;

	for (int i = 0; i < frequencies.size(); i++)
	{
		if (frequencies[i] >= max)
		{
			max = frequencies[i];
			maxPos = i;
		}
	}
	return values[maxPos];
}

// Complexity: Theta(length of the map)
// Best case: Theta(1) when the map does not have any element
// Worst case: O(length of the map) when the map has elements
MultiMap::~MultiMap() 
{
	node* current = this->head;
	while (current != NULL)
	{
		node* aux = current->next;
		delete current;
		current = aux;
	}
}

