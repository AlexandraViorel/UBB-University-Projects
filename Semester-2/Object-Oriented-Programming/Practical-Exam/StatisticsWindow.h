#pragma once

#include <QWidget>
#include "ui_StatisticsWindow.h"
#include "service.h"
#include "observer.h"

class StatisticsWindow : public QWidget, public Observer
{
	Q_OBJECT

public:
	StatisticsWindow(Service& s, QWidget *parent = Q_NULLPTR);
	~StatisticsWindow();
	void update() override;

private:
	Ui::StatisticsWindow ui;
	Service& serv;

	void populate();
};
