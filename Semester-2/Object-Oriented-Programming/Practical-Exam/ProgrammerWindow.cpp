#include "ProgrammerWindow.h"
#include <sstream>
#include <QMessageBox>

ProgrammerWindow::ProgrammerWindow(Programmer p, Service& s, QWidget *parent)
	: programmer{ p }, serv{ s }, QWidget(parent)
{
	ui.setupUi(this);
	QString title = QString::fromStdString(this->programmer.getName());
	this->setWindowTitle(title);
	this->serv.addObserver(this);
	this->populateList();
	this->connections();
	stillRevise = this->programmer.getTotalFilesToRevise() - this->programmer.getNoRevisedFiles();
	this->ui.revisedFilesLabel->setText(QString::fromStdString(std::to_string(this->serv.getProgRevisedServ(this->programmer.getName()))));
	this->ui.totalFilesLabel->setText(QString::fromStdString(std::to_string(stillRevise)));
	
}

ProgrammerWindow::~ProgrammerWindow()
{
}

void ProgrammerWindow::update()
{
	this->populateList();
	//this->ui.revisedFilesLabel->setText(QString::fromStdString(std::to_string(this->serv.getProgRevisedServ(this->programmer.getName()))));
	//this->ui.totalFilesLabel->setText(QString::fromStdString(std::to_string(this->serv.getProgTotalServ(this->programmer.getName()))));

}

void ProgrammerWindow::populateList()
{
	this->ui.filesListWidget->clear();
	std::vector<SourceFile> files = this->serv.getSortedFiles();
	for (auto f : files) {
		QString itemStr = QString::fromStdString(f.getName() + ";" + f.getStatus() + ";" + f.getCreator() + ";" + f.getReviewer());
		QListWidgetItem* item = new QListWidgetItem{ itemStr };
		if (f.getStatus() == "not_revised") {
			QFont font{};
			font.setBold(true);
			item->setFont(font);
		}
		if (f.getStatus() == "revised") {
			item->setBackground(Qt::green);
		}
		this->ui.filesListWidget->addItem(item);
	}
	//this->ui.revisedFilesLabel->setText(QString::fromStdString(std::to_string(this->serv.getProgRevisedServ(this->programmer.getName()))));
	//this->ui.totalFilesLabel->setText(QString::fromStdString(std::to_string(this->serv.getProgTotalServ(this->programmer.getName()))));
}

void ProgrammerWindow::connections()
{
	QWidget::connect(this->ui.addPushButton, &QPushButton::clicked, this, &ProgrammerWindow::handleAdd);
	QWidget::connect(this->ui.filesListWidget, &QListWidget::itemSelectionChanged, this, &ProgrammerWindow::handleSelection);
	QWidget::connect(this->ui.revisePushButton, &QPushButton::clicked, this, &ProgrammerWindow::handleRevise);
}

void ProgrammerWindow::handleSelection()
{
	std::string fileStr = this->ui.filesListWidget->currentItem()->text().toStdString();
	std::istringstream f(fileStr);
	std::string name, status, creator, reviewer;
	std::getline(f, name, ';');
	std::getline(f, status, ';');
	std::getline(f, creator, ';');
	std::getline(f, reviewer, ';');
	if (status == "not_revised" && this->serv.getFileCreatorServ(name) == this->programmer.getName() || status == "revised" || stillRevise == 0) {
		this->ui.revisePushButton->setEnabled(false);
	}
	else {
		this->ui.revisePushButton->setEnabled(true);
	}
}

void ProgrammerWindow::handleRevise()
{
	std::string fileStr = this->ui.filesListWidget->currentItem()->text().toStdString();
	std::istringstream f(fileStr);
	std::string name, status, creator, reviewer;
	std::getline(f, name, ';');
	std::getline(f, status, ';');
	std::getline(f, creator, ';');
	std::getline(f, reviewer, ';');
	this->serv.updateFileServ(name, "revised", this->programmer.getName());
	this->serv.updateProgrammerServ(this->programmer.getName());
	int revised = this->programmer.getNoRevisedFiles();
	revised++;
	this->programmer.setRevisedFiles(revised);
	stillRevise--;
	this->ui.revisedFilesLabel->setText(QString::fromStdString(std::to_string(this->serv.getProgRevisedServ(this->programmer.getName()))));
	this->ui.totalFilesLabel->setText(QString::fromStdString(std::to_string(stillRevise)));
	if (stillRevise == 0) {
		QMessageBox::information(this, "Congratulations", "Congratulations!");
	}
	QMessageBox::information(this, "Successful operation", "File revised successfully!");
	this->serv.notify();
}

void ProgrammerWindow::handleAdd()
{
	std::string fileName = this->ui.fileNameLineEdit->text().toStdString();
	if (fileName.empty()) {
		QMessageBox::critical(this, "Error", "File name cannot be empty!");
		return;
	}
	for (auto f : this->serv.getFilesServ()) {
		if (f.getName() == fileName) {
			QMessageBox::critical(this, "Error", "File name already used!");
			return;
		}
	}
	this->serv.addFileServ(fileName, "not_revised", this->programmer.getName(), "no");
	QMessageBox::information(this, "Successful operation", "File added successfully!");
	this->ui.fileNameLineEdit->clear();
	this->serv.notify();
}
