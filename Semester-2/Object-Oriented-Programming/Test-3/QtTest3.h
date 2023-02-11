#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_QtTest3.h"
#include "service.h"

class QtTest3 : public QMainWindow
{
    Q_OBJECT

public:
    QtTest3(Service& s, QWidget *parent = Q_NULLPTR);

private:
    Ui::QtTest3Class ui;

    Service& serv;

    void populateList();

    void connections();

    int getSelectedIndex();

    void addEq();

    void computeSols();
};
