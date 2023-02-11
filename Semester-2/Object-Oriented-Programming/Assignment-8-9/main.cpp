#include "UI.h"
#include <crtdbg.h>
#include "test.h"

int main()
{
	{
		testComparator();
		std::string fileName = "dogs.txt";
		Repository repo = Repository(fileName);
		repo.loadEntitiesFromFile();
		Service serv = Service(repo);
		UserService userServ = UserService();
		UI ui = UI(serv, userServ);
		ui.run();
	}
	_CrtDumpMemoryLeaks();
}
