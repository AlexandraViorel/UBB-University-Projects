#include "comparator.h"

ComparatorAscendingByAge::ComparatorAscendingByAge()
{
}

bool ComparatorAscendingByAge::compare(Dog el1, Dog el2)
{
    return el1.getAge() < el2.getAge();
}

ComparatorAscendingByAge::~ComparatorAscendingByAge() = default;

ComparatorAscendingByBreed::ComparatorAscendingByBreed()
{
}

bool ComparatorAscendingByBreed::compare(Dog el1, Dog el2)
{
    if (el1.getBreed().compare(el2.getBreed()) < 0) {
        return true;
    }
    return false;
}

ComparatorAscendingByBreed::~ComparatorAscendingByBreed() = default;
