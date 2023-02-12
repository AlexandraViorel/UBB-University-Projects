#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
using namespace std;

void SortedMap::resize()
{
	TElem* newInfo = new TElem[capacity * 2];
	int* newLeft = new int[capacity * 2];
	int* newRight = new int[capacity * 2];

	for (int i = 0; i < this->capacity; i++)
	{
		newInfo[i] = this->info[i];
		newLeft[i] = this->left[i];
		newRight[i] = this->right[i];
	}
	newLeft[firstEmpty] = this->capacity;
	for (int i = this->capacity; i < this->capacity * 2; i++)
	{
		newLeft[i] = i + 1;
	}
	newLeft[this->capacity * 2 - 1] = -1;

	TElem* oldInfo = this->info;
	int* oldLeft = this->left;
	int* oldRight = this->right;
	
	this->info = newInfo;
	this->left = newLeft;
	this->right = newRight;
	this->capacity *= 2;

	delete[] oldInfo;
	delete[] oldLeft;
	delete[] oldRight;
}

void SortedMap::initNode(int newPosition, TKey k, TValue v)
{
	this->info[newPosition] = TElem{ k, v };
	this->left[newPosition] = NULL_NODE;
	this->right[newPosition] = NULL_NODE;
}

std::pair<int, int> SortedMap::findMax(int current, int parent)
{
	while (this->right[current] != NULL_NODE) 
	{
		parent = current;
		current = this->right[current];
	}
	return { current, parent };
}

// Complexity: theta(initial capacity)
SortedMap::SortedMap(Relation r) 
{
	this->relation = r;

	this->capacity = INITIAL_CAPACITY;
	this->root = NULL_NODE;
	this->firstEmpty = 0;
	this->nrElements = 0;

	this->info = new TElem[INITIAL_CAPACITY];
	this->left = new int[INITIAL_CAPACITY];
	this->right = new int[INITIAL_CAPACITY];

	for (int i = 0; i < INITIAL_CAPACITY; i++)
	{
		this->info[i] = NULL_TPAIR;
		this->left[i] = i + 1;
	}
	this->left[INITIAL_CAPACITY - 1] = NULL_NODE;
}

TValue SortedMap::add(TKey k, TValue v) 
{
	if (this->left[firstEmpty] == NULL_NODE)
	{
		resize();
	}
	int newPosition = this->firstEmpty;

	// empty case
	if (this->root == NULL_NODE)
	{
		this->root = newPosition;
		this->firstEmpty = this->left[firstEmpty];
		this->initNode(newPosition, k, v);
	}
	else
	{
		int current = this->root;
		// we iterate until we find the key, or the current has no children on the respective side
		while (true)
		{
			// found key case
			if (this->info[current].first == k)
			{
				TValue oldValue = this->info[current].second;
				this->info[current].second = v;
				return oldValue;
			}
			// smaller key case (if "<" we go to the left)
			if (this->relation(k, this->info[current].first))
			{
				// if the current has no children to the left and k is "<", we put it to the left
				if (this->left[current] == NULL_NODE)
				{
					this->firstEmpty = this->left[firstEmpty];
					this->left[current] = newPosition;
					this->initNode(newPosition, k, v);
					break;
				}
				current = this->left[current];
			}
			// greater key case (if ">" we go to the right)
			else
			{
				// if the current has no children to the right and k is ">", we put it to the right
				if (this->right[current] == NULL_NODE)
				{
					this->firstEmpty = this->left[firstEmpty];
					this->right[current] = newPosition;
					this->initNode(newPosition, k, v);
					break;
				}
				current = this->right[current];
			}
		}
	}
	this->nrElements++;
	return NULL_TVALUE;
}

// Complexity: O(n), where n is the nb of elements of the map
TValue SortedMap::search(TKey k) const 
{
	int current = this->root;
	while (current != NULL_NODE && this->info[current].first != k)
	{
		if (this->relation(k, this->info[current].first))
		{
			current = this->left[current];
		}
		else
		{
			current = this->right[current];
		}
	}
	if (current != NULL_NODE)
	{
		return this->info[current].second;
	}
	return NULL_TVALUE;
}

TValue SortedMap::remove(TKey k) 
{
	if (this->root == NULL_NODE) return NULL_TVALUE;

	int parent = this->root, current = this->root;

	while (current != NULL_NODE) 
	{
		if (this->info[current].first == k) {
			// case 1: it has no children
			if (this->left[current] == NULL_NODE && this->right[current] == NULL_NODE) 
			{
				// we compare with the parent
				if (this->relation(this->info[current].first, this->info[parent].first)) 
				{
					// current < parent
					this->left[parent] = NULL_NODE;
				}
				else 
				{ 
					// current > parent
					this->right[parent] = NULL_NODE;
				}
				// the root case
				if (this->root == current)
					this->root = NULL_NODE;
			}
			// case 2.1: only one child - left child
			else if (this->left[current] != NULL_NODE && this->right[current] == NULL_NODE) 
			{
				// we compare with the parent
				if (this->relation(this->info[current].first, this->info[parent].first)) 
				{
					// current < parent
					this->left[parent] = this->left[current];
				}
				else 
				{ 
					// current > parent
					this->right[parent] = this->left[current];
				}
				// the root case
				if (this->root == current) 
					this->root = this->left[current];
			}
			// case 2.2: only one child - right child
			else if (this->left[current] == NULL_NODE && this->right[current] != NULL_NODE) 
			{
				// current < parent
				if (this->relation(this->info[current].first, this->info[parent].first)) 
				{
					this->left[parent] = this->right[current];
				}
				else 
				{ 
					// current > parent
					this->right[parent] = this->right[current];
				}
				// the root case
				if (this->root == current) 
					this->root = this->right[current];
			}
			// case 3: two children : we will find the maximum on the left subtree
			else 
			{
				// we find the max and check if the max has a child on the left side
				pair<int, int> maxFound = findMax(this->left[current], current);
				int max = maxFound.first, maxParent = maxFound.second;

				// case 3.1: the max is the child of current => we just move the right of the 
				// current to the max
				if (current == maxParent) 
				{
					this->right[max] = this->right[current];
				}
				// case 3.2: the max is not the child of the current
				else 
				{
					// if max has a left child, we move that to the right of its parent
					if (this->left[max] != NULL_NODE) 
					{
						this->right[maxParent] = this->left[max];
					}
					// otherwise, it is NULL_NODE
					else 
					{ 
						this->right[maxParent] = NULL_NODE;
					}
					// we change the max with the current node to be removed
					if (this->relation(this->info[current].first, this->info[parent].first)) 
					{ 
						// current < parent
						this->left[parent] = max;
					}
					else 
					{ 
						// current > parent
						this->right[parent] = max;
					}
					// we pass the children from current to max
					this->left[max] = this->left[current];
					this->right[max] = this->right[current];
				}
				// the root case
				if (this->root == current) 
					this->root = max;
			}
			// we move the first empty to this position
			this->left[current] = this->firstEmpty;
			this->firstEmpty = current;
			this->nrElements--;
			return this->info[current].second;
		}
		else if (this->relation(k, this->info[current].first)) {
			parent = current;
			current = this->left[current];
		}
		else {
			parent = current;
			current = this->right[current];
		}
	}
	return NULL_TVALUE;
}

int SortedMap::size() const 
{
	return this->nrElements;
}

bool SortedMap::isEmpty() const 
{
	return this->nrElements == 0;
}

void SortedMap::filter(Condition cond)
{
	SMIterator it = this->iterator();
	int current = it.currentNode;
	TElem el;
	while (current != NULL_NODE) {
		if (cond(this->info[current].second) == false) {
			el = this->info[current];
		}
		else {
			el = NULL_TPAIR;
		}
		it.next();
		current = it.currentNode;
		this->remove(el.first);
	}
}

SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}

SortedMap::~SortedMap() 
{
	delete[] this->info;
	delete[] this->left;
	delete[] this->right;
}
