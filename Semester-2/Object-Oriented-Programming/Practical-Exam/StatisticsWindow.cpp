#include "StatisticsWindow.h"

StatisticsWindow::StatisticsWindow(Service& s, QWidget *parent)
	: serv{ s }, QWidget(parent)
{
	ui.setupUi(this);
	this->serv.addObserver(this);
	this->populate();
}

StatisticsWindow::~StatisticsWindow()
{
}

void StatisticsWindow::update()
{
	this->populate();
}

void StatisticsWindow::populate()
{
	this->ui.programmersListWidget->clear();
	std::vector<Programmer> programmers = this->serv.getProgrammersServ();
	for (auto p : programmers) {
		QString itemStr = QString::fromStdString(p.getName() + "; revised files: " + std::to_string(p.getNoRevisedFiles()));
		QListWidgetItem* item = new QListWidgetItem{ itemStr };
		if (p.getTotalFilesToRevise() - p.getNoRevisedFiles() == 0) {
			item->setForeground(Qt::blue);
		}
		this->ui.programmersListWidget->addItem(item);
	}
}
