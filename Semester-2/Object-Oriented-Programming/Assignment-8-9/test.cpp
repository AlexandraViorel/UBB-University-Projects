#include "test.h"
#include <vector>
#include <cassert>

void testComparator()
{
	Dog d1 = Dog("Yoda", "German Shepherd", 1, "https://en.wikipedia.org/wiki/German_Shepherd#/media/File:German_Shepherd_-_DSC_0346_(10096362833).jpg");
	Dog d2 = Dog("Rex", "Husky", 5, "https://ro.wikipedia.org/wiki/Husky_Siberian#/media/Fi%C8%99ier:Siberian-husky.jpg");
	Dog d3 = Dog("Bruno", "Labrador Retriever", 2, "https://en.wikipedia.org/wiki/Labrador_Retriever#/media/File:Labrador_on_Quantock_(2175262184).jpg");

	std::vector<Dog> dogsList;
	dogsList.push_back(d1);
	dogsList.push_back(d2);
	dogsList.push_back(d3);

	auto *c1 = new ComparatorAscendingByAge();
	std::vector<Dog> v1 = sortFunction(dogsList, *c1);
	assert(v1[0].getAge() == 1);
	assert(v1[1].getAge() == 2);
	assert(v1[2].getAge() == 5);

	auto* c2 = new ComparatorAscendingByBreed();
	std::vector<Dog> v2 = sortFunction(dogsList, *c2);
	assert(v2[0].getBreed() == "German Shepherd");
	assert(v2[1].getBreed() == "Husky");
	assert(v2[2].getBreed() == "Labrador Retriever");

	delete c1;
	delete c2;
}
