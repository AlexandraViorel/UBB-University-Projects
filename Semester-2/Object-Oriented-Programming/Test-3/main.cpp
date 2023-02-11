#include "QtTest3.h"
#include <QtWidgets/QApplication>
#include "repository.h"
#include "service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Repository r{ "data.txt" };
    r.loadFromFile();
    Service s{ r };
    QtTest3 w{ s };
    w.show();
    return a.exec();
}
