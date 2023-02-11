#pragma once

#include <QWidget>
#include "ui_ProgrammerWindow.h"
#include "service.h"

class ProgrammerWindow : public QWidget, public Observer
{
	Q_OBJECT

public:
	ProgrammerWindow(Programmer p, Service& s, QWidget *parent = Q_NULLPTR);
	~ProgrammerWindow();

	void update() override;

private:
	Ui::ProgrammerWindow ui;

	Programmer programmer;
	Service& serv;
	int stillRevise;

	void populateList();
	void connections();

	void handleSelection();
	void handleRevise();
	void handleAdd();
};
