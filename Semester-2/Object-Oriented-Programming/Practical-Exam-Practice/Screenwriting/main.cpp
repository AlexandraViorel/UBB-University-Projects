//#include "screenwriting.h"
#include <QtWidgets/QApplication>
#include "WriterWindow.h"
#include "repository.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    /*screenwriting w;
    w.show();*/
    Repository repo;
    WriterTableModel* model = new WriterTableModel{ repo };
    for (auto w : repo.getWriters()) {
        WriterWindow* win = new WriterWindow{ w, repo, model };
        win->show();
    }
    return a.exec();
}
