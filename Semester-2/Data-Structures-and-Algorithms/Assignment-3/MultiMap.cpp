#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;

// Complexity: Theta(capacity)
MultiMap::MultiMap() {
	this->mmap.capacity = 10;
	this->mmap.nodes = new SLLANode[10];
	this->mmap.head = -1;
	for (int i = 0; i < this->mmap.capacity - 1; i++) {
		this->mmap.nodes[i].next = i + 1;
	}
	this->mmap.nodes[this->mmap.capacity - 1].next = -1;
	this->mmap.firstEmpty = 0;
	this->mmap.length = 0;
}

// Complexity: O(length of the multimap)
// BC: Theta(1) if the multimap is empty
// WC: O(length of the multimap)
void MultiMap::add(TKey c, TValue v) {
	if (this->mmap.length == 0) {
		int pos = this->mmap.firstEmpty;
		this->mmap.nodes[pos].k = c;

		// here we put the value in the empty SideSLLA 
		SideSLLA& side = this->mmap.nodes[pos].el;
		int fe = side.firstEmpty;
		side.values[fe].v = v;
		side.firstEmpty = side.values[side.firstEmpty].next;
		side.values[fe].next = -1;
		side.head = fe;
		side.length++;
		
		this->mmap.firstEmpty = this->mmap.nodes[this->mmap.firstEmpty].next;

		this->mmap.nodes[pos].next = this->mmap.head;
		//this->mmap.nodes[this->mmap.head].next = copyFirstEmpty;
		this->mmap.head = pos;
		this->mmap.length++;
		return;
	}
	else
	{
		int node = this->mmap.head;
		int previousNode = -1;
		while (node != -1 && this->mmap.nodes[node].k != c) {
			previousNode = node;
			node = this->mmap.nodes[node].next;
		}
		if (node != -1) {
			// here the key already exists in the main SLLA and we add the element in the SideSLLA
			SideSLLA& side = this->mmap.nodes[node].el;
			// if the SideSLLA is full we increase its capacity
			if (side.length == side.capacity && side.firstEmpty == -1) {
				side.capacity *= 2;
				auto* aux = new SideSLLANode[side.capacity];
				for (int i = 0; i < side.length; i++) {
					aux[i] = side.values[i];
				}
				delete[] side.values;
				side.values = aux;
				for (int i = side.length; i < side.capacity - 1; i++) {
					side.values[i].next = i + 1;
				}
				side.values[side.capacity - 1].next = -1;
			}
			if (side.firstEmpty == -1) {
				side.firstEmpty = side.length;
				side.values[side.firstEmpty].v = v;
				side.values[side.firstEmpty].next = -1;
				side.length++;
			}
			int pos = side.firstEmpty;
			side.values[pos].v = v;
			side.firstEmpty = side.values[side.firstEmpty].next;
			side.values[pos].next = side.head;
			side.head = pos;
			side.length++;
			return;
		}
		else {
			// we check if the SLLA is full, and we increase its capacity if it is full
			if (this->mmap.length == this->mmap.capacity && this->mmap.firstEmpty == -1) {
				this->mmap.capacity *= 2;
				auto* aux = new SLLANode[this->mmap.capacity];
				for (int i = 0; i < this->mmap.length; i++) {
					aux[i] = this->mmap.nodes[i];
				}
				delete[] this->mmap.nodes;
				this->mmap.nodes = aux;
				for (int i = this->mmap.length; i < this->mmap.capacity - 1; i++) {
					this->mmap.nodes[i].next = i + 1;
				}
				this->mmap.nodes[this->mmap.capacity - 1].next = -1;
				this->mmap.firstEmpty = this->mmap.length;
			}
			if (this->mmap.firstEmpty == -1) {
				this->mmap.firstEmpty = this->mmap.length;
				this->mmap.nodes[this->mmap.firstEmpty].k = c;
				this->mmap.nodes[this->mmap.firstEmpty].next = -1;
				this->mmap.length++;
				int copyFirstEmpty = this->mmap.firstEmpty;
				SideSLLA& side = this->mmap.nodes[copyFirstEmpty].el;
				int fe = side.firstEmpty;
				side.values[fe].v = v;
				side.firstEmpty = side.values[side.firstEmpty].next;
				side.values[fe].next = -1;
				side.head = fe;
				side.length++;
				this->mmap.nodes[copyFirstEmpty].next = this->mmap.head;
				this->mmap.head = copyFirstEmpty;
			}
			// here we create a new SideSLLA
			int copyFirstEmpty = this->mmap.firstEmpty;
			this->mmap.firstEmpty = this->mmap.nodes[this->mmap.firstEmpty].next;
			this->mmap.nodes[copyFirstEmpty].k = c;

			// here we put the value in the empty SideSLLA 
			SideSLLA& side = this->mmap.nodes[copyFirstEmpty].el;
			int fe = side.firstEmpty;
			side.values[fe].v = v;
			side.firstEmpty = side.values[side.firstEmpty].next;
			side.values[fe].next = -1;
			side.head = fe;
			side.length++;

			this->mmap.nodes[copyFirstEmpty].next = this->mmap.head;
			this->mmap.head = copyFirstEmpty;
			this->mmap.length++;
			return;
		}
	}
}


bool MultiMap::remove(TKey c, TValue v) {
	//if (this->isEmpty()) {
	//	return false;
	//}
	//int node = this->mmap.head;
	//int previousNode = -1;
	//while (node != -1 && this->mmap.nodes[node].k != c) {
	//	previousNode = node;
	//	node = this->mmap.nodes[node].next;
	//}
	//if (node != -1) {
	//	// we found the given key
	//	SideSLLA& side = this->mmap.nodes[node].el;
	//	int sideNode = side.head;
	//	int sidePrevious = -1;
	//	while (sideNode != -1 && side.values[sideNode].v != v) {
	//		sidePrevious = sideNode;
	//		sideNode = side.values[sideNode].next;
	//	}
	//	if (sideNode != -1) {
	//		// we found the given value
	//		if (side.length == 1) {
	//			// if the key has only the value that must be deleted, we also must delete the key
	//			//if (node == this->mmap.head) {
	//			//	this->mmap.head = this->mmap.nodes[this->mmap.head].next;
	//			//}
	//			//else {
	//			//	this->mmap.nodes[previousNode].next = this->mmap.nodes[node].next;
	//			//}
	//			//this->mmap.nodes[node].next = this->mmap.firstEmpty;
	//			//this->mmap.firstEmpty = node;
	//			//this->mmap.length--;
	//			//side.values[sideNode].next = side.firstEmpty;
	//			//side.firstEmpty = sideNode;
	//			//side.length--;
	//			//return true;
	//			this->mmap.nodes[previousNode].next = this->mmap.nodes[node].next;
	//			this->mmap.firstEmpty = node;
	//			this->mmap.length--;
	//			side.firstEmpty = sideNode;
	//			side.length--;
	//			return true;
	//		}
	//		else {
	//			// we only delete the given value from the SideSLLA
	//			if (sideNode == side.head) {
	//				side.head = side.values[side.head].next;
	//			}
	//			else {
	//				side.values[sidePrevious].next = side.values[sideNode].next;
	//			}
	//			side.values[sideNode].next = side.firstEmpty;
	//			side.firstEmpty = sideNode;
	//			side.length--;
	//			return true;
	//		}
	//	}
	//	else {
	//		// we did not find the given value
	//		return false;
	//	}
	//}
	//else {
	//	// we did not find the given key
	//	return false;
	//}

	if (this->isEmpty()) {
		return false;
	}
	if (this->mmap.length == 1) {
		if (this->mmap.nodes[this->mmap.head].k == c) {
			SideSLLA& side = this->mmap.nodes[mmap.head].el;
			if (side.length == 1) {
				if (side.values[side.head].v == v) {
					// in this case the multimap becomes empty
					side.values[side.head].next = side.firstEmpty;
					side.firstEmpty = side.head;
					side.head = -1;
					side.length--;
					mmap.nodes[mmap.head].next = mmap.firstEmpty;
					mmap.firstEmpty = mmap.head;
					mmap.head = -1;
					mmap.length--;
					return true;
				}
				else {
					// we did not find the value
					return false;
				}
			}
			else {
				int sideNode = side.head;
				int sidePrevious = -1;
				while (sideNode != -1 && side.values[sideNode].v != v) {
					sidePrevious = sideNode;
					sideNode = side.values[sideNode].next;
				}
				if (sideNode != -1) {
					// we found the given value
					if (sideNode == side.head) {
						side.head = side.values[side.head].next;
						side.length--;
					}
					else {
						side.values[sidePrevious].next = side.values[sideNode].next;
						side.length--;
					}
					side.values[sideNode].next = side.firstEmpty;
					side.firstEmpty = sideNode;
					return true;
				}
				else {
					// we did not find the given value
					return false;
				}
			}
		}
		else {
			// the did not find the given key
			return false;
		}
	}
	else {
		int node = this->mmap.head;
		int previousNode = -1;
		while (node != -1 && this->mmap.nodes[node].k != c) {
			previousNode = node;
			node = this->mmap.nodes[node].next;
		}
		if (node != -1) {
			// we found the given key
			SideSLLA& side = this->mmap.nodes[node].el;
			if (side.length == 1) {
				if (side.values[side.head].v == v) {
					// we found the given value, in this case the SideSLLA becomes empty
					side.values[side.head].next = side.firstEmpty;
					side.firstEmpty = side.head;
					side.head = -1;
					side.length--;
					if (node == mmap.head) {
						mmap.head = mmap.nodes[mmap.head].next;
						mmap.length--;
					}
					else {
						mmap.nodes[previousNode].next = mmap.nodes[node].next;
						mmap.length--;
					}
					mmap.nodes[node].next = mmap.firstEmpty;
					mmap.firstEmpty = node;
					return true;
				}
				else {
					// we did not find the given value
					return false;
				}
			}
			else {
				SideSLLA& side = this->mmap.nodes[node].el;
				int sideNode = side.head;
				int sidePrevious = -1;
				while (sideNode != -1 && side.values[sideNode].v != v) {
					sidePrevious = sideNode;
					sideNode = side.values[sideNode].next;
				}
				if (sideNode != -1) {
					// we found the given value
					if (sideNode == side.head) {
						side.head = side.values[side.head].next;
						side.length--;
					}
					else {
						side.values[sidePrevious].next = side.values[sideNode].next;
						side.length--;
					}
					side.values[sideNode].next = side.firstEmpty;
					side.firstEmpty = sideNode;
					return true;
				}
				else {
					// we did not find the given value
					return false;
				}
			}
		}
		else {
			// we did not find the given key
			return false;
		}
	}
}

// Complexity: O(length of the multimap)
vector<TValue> MultiMap::search(TKey c) const {
	vector<TValue> vec = vector<TValue>();
	int pos = this->mmap.head;
	while (pos != -1 && this->mmap.nodes[pos].k != c) {
		pos = this->mmap.nodes[pos].next;
	}
	if (pos != -1) {
		SideSLLA& side = this->mmap.nodes[pos].el;
		int sidePos = side.head;
		while (sidePos != -1) {
			vec.push_back(side.values[sidePos].v);
			sidePos = side.values[sidePos].next;
		}
	}
	return vec;
}


int MultiMap::size() const {
	int len = 0;
	int pos = this->mmap.head;
	while (pos != -1) {
		//std::cout << mmap.nodes[pos].k << " " << mmap.nodes[pos].el.length << "\n";
		len = len + mmap.nodes[pos].el.length;
		pos = this->mmap.nodes[pos].next;
	}
	return len;
}


bool MultiMap::isEmpty() const {
	return this->mmap.length == 0;
}

MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}


MultiMap::~MultiMap() {
	delete[] this->mmap.nodes;
}

SLLANode::SLLANode()
{
	this->k = NULL_TVALUE;
	this->el = SideSLLA();
	this->next = 0;
}

SideSLLANode::SideSLLANode()
{
	this->v = NULL_TVALUE;
	this->next = 0;
}

SideSLLA::SideSLLA()
{
	this->capacity = 10;
	this->firstEmpty = 0;
	this->head = -1;
	this->values = new SideSLLANode[10];
	for (int i = 0; i < this->capacity; i++) {
		this->values[i].next = i + 1;
	}
	this->values[this->capacity - 1].next = -1;
	this->length = 0;
}
