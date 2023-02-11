#include "Tests.h"
#include <cassert>
#include "Errors.h"
#include <iostream>


void testDomain()
{
	Dog testDog("Rex", "Husky", 3, "https://ro.wikipedia.org/wiki/Husky_Siberian#/media/Fi%C8%99ier:Siberian-husky.jpg");
	assert(testDog.getBreed() == "Husky");
	assert(testDog.getName() == "Rex");
	assert(testDog.getAge() == 3);
	assert(testDog.getPhotoLink() == "https://ro.wikipedia.org/wiki/Husky_Siberian#/media/Fi%C8%99ier:Siberian-husky.jpg");
}

void testDynamicArray()
{
	DynamicArray<Dog> arr{ 20 };
	assert(arr.lengthGetter() == 0);
	assert(arr.capacityGetter() == 20);

	Dog d1 = Dog();
	d1.setName("abc");
	arr.addElement(d1);
	assert(arr.lengthGetter() == 1);
	assert(arr[0].getName() == "abc");

	Dog d2 = Dog();
	d2.setName("abcd");
	arr.addElement(d2);
	assert(arr.lengthGetter() == 2);

	arr.deleteElement(0);
	assert(arr.lengthGetter() == 1);
	assert(arr[0].getName() == "abcd");

	DynamicArray<int> arr2;
	for (int i = 0; i < 100; i++)
	{
		arr2.addElement(i);
	}
	assert(arr2.lengthGetter() == 100);

	arr2 = arr2;

	arr2.deleteElement(500);

}

void testRepo()
{
	Dog d1 = Dog();
	d1.setName("abc");

	Dog d2 = Dog();
	d2.setName("abcd");
	d2.setAge(4);

	Dog d3 = Dog();
	d3.setName("abc");

	Repository repo = Repository();
	repo.addDogRepo(d1);
	repo.addDogRepo(d2);

	std::vector<Dog> arr = repo.getDogList();
	assert(arr[0].getName() == "abc");

	try 
	{
		repo.addDogRepo(d3);
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	Dog d4 = Dog();
	d4.setName("abcdef");

	repo.updateDogRepo("abc", d4);
	assert(repo.getDogList()[0].getName() == "abcdef");

	try
	{
		repo.updateDogRepo("a", d4);
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	repo.deleteDogRepo(d4.getName());
	assert(repo.getDogList()[0].getName() == "abcd");
	assert(repo.findDogRepo("abcd").getAge() == 4);

	try
	{
		repo.deleteDogRepo("a");
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	Repository repo2 = Repository(repo);
}

void testUserRepo()
{
	Dog d1 = Dog();
	d1.setName("abc");
	d1.setAge(5);

	Dog d2 = Dog();
	d2.setName("abcd");
	d2.setAge(4);

	Dog d3 = Dog();
	d3.setName("abc");

	AdoptingRepository repo = AdoptingRepository();
	repo.add(d1);
	repo.add(d2);

	std::vector<Dog> arr = repo.getAdoptingList();
	assert(arr[0].getName() == "abc");

	try
	{
		repo.add(d3);
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	Dog d4 = Dog();
	d4.setName("abcdef");

	repo.remove(d2.getName());
	assert(repo.getAdoptingList()[0].getName() == "abc");
	assert(repo.findDod("abc").getAge() == 5);

	try
	{
		repo.remove("a");
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	AdoptingRepository repo2 = AdoptingRepository(repo);
}

void testService()
{
	Repository repo = Repository();
	Service serv = Service(repo);

	serv.add("abc", "a", 5, "link");
	assert(serv.getDogList()[0].getName() == "abc");
	serv.add("abcd", "ab", 6, "link1");
	assert(serv.getDogList()[1].getName() == "abcd");

	try
	{
		serv.add("abc", "ab", 2, "link2");
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	try
	{
		serv.remove("e");
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	serv.remove("abc");
	assert(serv.getDogList()[0].getName() == "abcd");

	serv.update("abcd", "bac", 9, "linkk");
	assert(serv.getDogList()[0].getBreed() == "bac");

	try
	{
		serv.update("e", "bac", 3, "link1");
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

}

void testUserService()
{
	AdoptingRepository repo = AdoptingRepository();
	UserService serv = UserService(repo);

	serv.add("abc", "a", 5, "link");
	assert(serv.getAdoptingList()[0].getName() == "abc");
	serv.add("abcd", "ab", 6, "link1");
	assert(serv.getAdoptingList()[1].getName() == "abcd");

	try
	{
		serv.add("abc", "ab", 2, "link2");
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	try
	{
		serv.remove("e");
		assert(false);
	}
	catch (RepoError)
	{
		assert(true);
	}

	serv.remove("abc");
	assert(serv.getAdoptingList()[0].getName() == "abcd");
}

void runAllTests()
{
	testDomain();
	testDynamicArray();
	testRepo();
	testUserRepo();
	testService();
	testUserService();
}
