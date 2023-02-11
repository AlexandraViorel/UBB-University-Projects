#pragma once

#include <QWidget>
#include "ui_DevelopWindow.h"
#include "idea.h"

class DevelopWindow : public QWidget
{
	Q_OBJECT

public:
	DevelopWindow(Idea i, QWidget *parent = Q_NULLPTR);
	~DevelopWindow();

private:
	Ui::DevelopWindow ui;
	Idea idea;

	void connect();

	void save();
};
