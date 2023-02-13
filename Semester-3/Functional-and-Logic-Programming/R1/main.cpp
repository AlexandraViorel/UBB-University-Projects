#include "lista.h"
#include <iostream>

bool search(Lista l, TElem el) {
	if (checkEmpty(l)) {
		return false;
	}
	if (firstElem(l) == el) {
		return true;
	}
	return search(listFromSecond(l), el);
}

Lista listToSet(Lista l) {
	if (checkEmpty(l))
		return voidList();
	TElem el = firstElem(l);
	if (!search(listFromSecond(l), el)) {
		return add(listToSet(listFromSecond(l)), el);
	}
	return listToSet(listFromSecond(l));
}

Lista intersection(Lista a, Lista b) {
	if (checkEmpty(a))
		return voidList();
	if (checkEmpty(b))
		return voidList();
	TElem el = firstElem(a);
	if (search(b, el)) {
		return add(intersection(listFromSecond(a), b), el);
	}
	return intersection(listFromSecond(a), b);
}

int main()
{
   Lista l1, l2;
   l1 = creare();
   tipar(l1);
   std::cout << "\n";
   l2 = creare();
   tipar(l2);
   std::cout << "\n";
   bool areEqual = equal(l1, l2);
   if (areEqual) {
	   std::cout << "the lists are equal\n";
   }
   else {
	   std::cout << "the lists are not equal\n";
   }
   l1 = listToSet(l1);
   l2 = listToSet(l2);
   Lista rez = intersection(l1, l2);
   std::cout << "Intersection:";
   tipar(rez);
}
