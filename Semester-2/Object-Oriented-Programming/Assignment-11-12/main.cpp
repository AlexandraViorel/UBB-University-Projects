#include <qapplication.h>
#include <qpushbutton.h>
#include "service.h"
#include "repository.h"
#include "domain.h"
#include <vector>
#include <crtdbg.h>
#include "QtWidgetsApplication1.h"

int main(int argc, char *argv[])
{
	QApplication app(argc, argv);
	std::string fileName = "dogs.txt";
	Repository repo = Repository(fileName);
	repo.loadEntitiesFromFile();
	Service serv{ repo };
	UserService userServ;

	QtWidgetsApplication1 gui{serv, userServ};
	gui.show();

	return app.exec();

}
