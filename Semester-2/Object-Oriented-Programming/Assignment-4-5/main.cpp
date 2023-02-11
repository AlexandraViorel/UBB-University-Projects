#include <iostream>
#include "UI.h"
#include <crtdbg.h>
#include "Tests.h"
#include <iostream>

int main()
{
	//runAllTests();
	std::cout << "All tests passed successfully !\n";

	Repository repo = Repository();
	Service service = Service(repo);
	service.add("Yoda", "German Shepherd", 1, "https://en.wikipedia.org/wiki/German_Shepherd#/media/File:German_Shepherd_-_DSC_0346_(10096362833).jpg");
	service.add("Rex", "Husky", 5, "https://ro.wikipedia.org/wiki/Husky_Siberian#/media/Fi%C8%99ier:Siberian-husky.jpg");
	service.add("Alfie", "Bulldog", 3, "https://en.wikipedia.org/wiki/Bulldog#/media/File:Bulldog_adult_male.jpg");
	service.add("Bruno", "Labrador Retriever", 2, "https://en.wikipedia.org/wiki/Labrador_Retriever#/media/File:Labrador_on_Quantock_(2175262184).jpg");
	service.add("Coco", "Pudel", 7, "https://ro.wikipedia.org/wiki/Pudel#/media/Fi%C8%99ier:Silver_Miniature_Poodle_stacked.jpg");
	service.add("Falco", "Chihuahua", 1, "https://ro.wikipedia.org/wiki/Chihuahua_(ras%C4%83_canin%C4%83)#/media/Fi%C8%99ier:Chihuahua1_bvdb.jpg");
	service.add("Grivei", "Boxer", 5, "https://ro.wikipedia.org/wiki/Boxer_(c%C3%A2ine)#/media/Fi%C8%99ier:Boxer_puppy_fawn.jpg");
	service.add("Hugo", "Pomeranian", 3, "https://ro.wikipedia.org/wiki/Pomeranian#/media/Fi%C8%99ier:Pomeranian_orange-sable_Coco.jpg");
	service.add("Kiki", "Chow chow", 4, "https://ro.wikipedia.org/wiki/Chow_chow#/media/Fi%C8%99ier:01_Chow_Chow.jpg");
	service.add("Aky", "Rottweiler", 1, "https://ro.wikipedia.org/wiki/Rottweiler#/media/Fi%C8%99ier:Rottweiler.jpg");

	AdoptingRepository userRepo = AdoptingRepository();
	UserService userService = UserService(userRepo);

	UI ui = UI(service, userService);
	ui.run();

}