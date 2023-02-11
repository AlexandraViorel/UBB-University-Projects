#pragma once
#ifndef NOMINMAX
#define NOMINMAX
#include <QtWidgets/QMainWindow>
#include "ui_QtWidgetsApplication1.h"
#include "service.h"
#include "userService.h"

class QtWidgetsApplication1 : public QMainWindow
{
    Q_OBJECT

public:
    QtWidgetsApplication1(Service& s, UserService& u, QWidget *parent = Q_NULLPTR);

private:
    Ui::QtWidgetsApplication1Class ui;
    Service& serv;
    UserService& userServ;

    QWidget* chartWindow;

    bool userRepoTypeSelected;

    void connectSignalsAndSlots();

    int getSelectedIndex() const;

    void populateDogsList(std::string filterText);

    void addDog();

    void deleteDog();

    void updateDog();

    void filterDogs();

    int getSelectedIndexUser() const;

    void populateDogsListUser(std::string filterText, int ageFilter);

    void filterDogsUser();

    void populateAdoptingList();

    void adoptDog();

    void makeCharts();
};

#endif // !NOMINMAX
