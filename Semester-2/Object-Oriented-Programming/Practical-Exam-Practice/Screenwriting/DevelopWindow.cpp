#include "DevelopWindow.h"
#include <fstream>

DevelopWindow::DevelopWindow(Idea i, QWidget *parent)
	: idea{ i }, QWidget(parent)
{
	ui.setupUi(this);
	this->connect();
}

DevelopWindow::~DevelopWindow()
{
}

void DevelopWindow::connect()
{
	QWidget::connect(this->ui.savePushButton, &QPushButton::clicked, this, &DevelopWindow::save);
}

void DevelopWindow::save()
{
	std::ofstream f("1.txt");
	f << this->ui.textEdit->toPlainText().toStdString();
 	f.close();
}
