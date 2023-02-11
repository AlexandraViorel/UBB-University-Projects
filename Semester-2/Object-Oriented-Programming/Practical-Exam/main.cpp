#include "practicalExam.h"
#include <QtWidgets/QApplication>
#include "ProgrammerWindow.h"
#include "service.h"
#include "programmersRepo.h"
#include "sourceFilesRepo.h"
#include "StatisticsWindow.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ProgrammerRepo pRepo{};
    SourceFilesRepo fRepo{};
    Service serv{ pRepo, fRepo };
    StatisticsWindow* win = new StatisticsWindow{ serv };
    win->show();
    std::vector<ProgrammerWindow*> windows;
    for (auto p : serv.getProgrammersServ()) {
        ProgrammerWindow* w = new ProgrammerWindow{ p, serv };
        w->show();
        windows.push_back(w);
    }
    return a.exec();
}
