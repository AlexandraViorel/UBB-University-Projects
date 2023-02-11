#include "MultiMapIterator.h"
#include "MultiMap.h"


MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
	this->currentPositionSLLA = col.mmap.head;
	this->currentPositionSideSLLA = col.mmap.nodes[currentPositionSLLA].el.head;
}

// Complexity: Theta(1)
TElem MultiMapIterator::getCurrent() const{
	if (valid()) {
		TKey k = col.mmap.nodes[currentPositionSLLA].k;
		TValue v = col.mmap.nodes[currentPositionSLLA].el.values[currentPositionSideSLLA].v;
		TElem e = std::make_pair(k, v);
		return e;
	}
	else {
		throw exception();
	}

}

// Complexity: Theta(1)
bool MultiMapIterator::valid() const {
	return (this->currentPositionSLLA != -1 && this->currentPositionSideSLLA != -1);
}

// Complexity: Theta(1)
void MultiMapIterator::next() {
	if (!this->valid())
	{
		throw std::exception();
	}
	this->currentPositionSideSLLA = col.mmap.nodes[currentPositionSLLA].el.values[currentPositionSideSLLA].next;
	if (this->currentPositionSideSLLA == -1) {
		this->currentPositionSLLA = col.mmap.nodes[currentPositionSLLA].next;
		if (this->currentPositionSLLA != -1) {
			this->currentPositionSideSLLA = col.mmap.nodes[currentPositionSLLA].el.head;
		}
	}
}

// Complexity: Theta(1)
void MultiMapIterator::first() {
	this->currentPositionSLLA = this->col.mmap.head;
	this->currentPositionSideSLLA = col.mmap.nodes[currentPositionSLLA].el.head;
}

TElem MultiMapIterator::remove()
{
	if (!valid()) {
		throw exception();
	}
	TElem current = this->getCurrent();
	return TElem();
}

