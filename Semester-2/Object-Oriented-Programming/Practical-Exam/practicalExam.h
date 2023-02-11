#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_practicalExam.h"

class practicalExam : public QMainWindow
{
    Q_OBJECT

public:
    practicalExam(QWidget *parent = Q_NULLPTR);

private:
    Ui::practicalExamClass ui;
};
