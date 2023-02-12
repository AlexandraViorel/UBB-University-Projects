#pragma once
#include "SortedMap.h"
#define STACK_INITIAL_CAPACITY 30

//DO NOT CHANGE THIS PART
class SMIterator{
	friend class SortedMap;
private:
	const SortedMap& map;
	SMIterator(const SortedMap& mapionar);

	int currentNode;
	int* nodeStack;
	int stackCapacity;
	int stackSize;

	void resizeStack();

public:
	void first();
	void next();
	bool valid() const;
    TElem getCurrent() const;
	~SMIterator();
};

