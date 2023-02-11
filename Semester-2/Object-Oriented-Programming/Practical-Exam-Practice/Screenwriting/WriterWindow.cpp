#include "WriterWindow.h"
#include <QMessageBox>
#include <fstream>

WriterWindow::WriterWindow(Writer writer, Repository& repo, WriterTableModel* model, QWidget *parent)
	: writer{ writer }, repo{ repo }, model{ model }, QWidget(parent)
{
	ui.setupUi(this);
	QString title = QString::fromStdString(this->writer.getName());
	this->setWindowTitle(title);
	//this->model = new WriterTableModel{ this->repo };
	this->initialize();
	this->connections();

}

WriterWindow::~WriterWindow()
{
}

void WriterWindow::initialize()
{
	this->ui.tableView->setModel(this->model);
	this->ui.tableView->resizeColumnsToContents();
	if (this->writer.getExpertise() != "senior") {
		this->ui.acceptIdeaPushButton->setEnabled(false);
	}
	std::vector<Idea> accIdeas = this->repo.getAcceptedIdeas(this->writer);
	if (accIdeas.empty())
		this->ui.developPushButton->setEnabled(false);
}

void WriterWindow::connections()
{
	QWidget::connect(this->ui.addIdeaPushButton, &QPushButton::clicked, this, &WriterWindow::handleAddIdea);

	//QWidget::connect(this->ui.tableView, &QTableView::)

	QWidget::connect(this->ui.acceptIdeaPushButton, &QPushButton::clicked, this, &WriterWindow::handleAcceptIdea);

	QWidget::connect(this->ui.developPushButton, &QPushButton::clicked, this, &WriterWindow::handleDevelop);

	QWidget::connect(this->ui.savePlotPushButton, &QPushButton::clicked, this, &WriterWindow::handleSavePlot);
}

void WriterWindow::handleAddIdea()
{
	try
	{
		std::string desc = this->ui.descriptionLineEdit->text().toStdString();
		int act = this->ui.actLineEdit->text().toInt();
		if (desc.empty()) {
			QMessageBox::critical(this, "Error", "Description cannot be empty!");
			this->ui.descriptionLineEdit->clear();
			this->ui.actLineEdit->clear();
			return;
		}
		if (act != 1 && act != 2 && act != 3) {
			QMessageBox::critical(this, "Error", "Act can be only 1, 2 or 3!");
			this->ui.descriptionLineEdit->clear();
			this->ui.actLineEdit->clear();
			return;
		}
		Idea i{ desc, "proposed", this->writer.getName(), act };
		this->model->addIdea(i);
		this->ui.descriptionLineEdit->clear();
		this->ui.actLineEdit->clear();
		QMessageBox::information(this, "Successfull operation", "Idea added successfully!");
	}
	catch (const std::exception&)
	{
		QMessageBox::critical(this, "Error", "An idea with the same description already exists!");
		this->ui.descriptionLineEdit->clear();
		this->ui.actLineEdit->clear();
		return;
	}
}

int WriterWindow::getSelectedIndex() const
{
	QModelIndexList selectedIndexes = this->ui.tableView->selectionModel()->selectedIndexes();
	if (selectedIndexes.size() == 0)
	{
		this->ui.descriptionLineEdit->clear();
		this->ui.actLineEdit->clear();
		return -1;
	}
	int selectedIndex = selectedIndexes.at(0).row();
	return selectedIndex;
}

void WriterWindow::handleAcceptIdea()
{
	int selectedIndex = this->getSelectedIndex();
	if (selectedIndex < 0)
	{
		QMessageBox::critical(this, "Error", "Please select an idea to revise and accept !");
		return;
	}
	Idea i = this->repo.getIdeas()[selectedIndex];
	if (i.getStatus() == "accepted") {
		QMessageBox::critical(this, "Error", "Idea already accepted!");
		return;
	}
	this->model->updateIdea(i);
	QMessageBox::information(this, "Status updated", "Idea accepted successfully!");

}

void WriterWindow::handleDevelop()
{
	std::vector<Idea> accIdeas = this->repo.getAcceptedIdeas(this->writer);
	if (accIdeas.empty()) {
		QMessageBox::critical(this, "Error", "Writer has no accepted ideas!");
		return;
	}
	for (auto i : accIdeas) {
		DevelopWindow* w = new DevelopWindow{ i };
		w->show();
	}
}

void WriterWindow::handleSavePlot()
{
	std::vector<Idea> ideas = this->repo.getIdeas();
	std::ofstream f("plot.txt");
	f << "Act 1\n";
	for (auto i : ideas) {
		if (i.getAct() == 1 && i.getStatus() == "accepted") {
			f << i.getDescription() << " {" << i.getCreator() << "}\n";
		}
	}
	f << "Act 2\n";
	for (auto i : ideas) {
		if (i.getAct() == 2 && i.getStatus() == "accepted") {
			f << i.getDescription() << " {" << i.getCreator() << "}\n";
		}
	}
	f << "Act 3\n";
	for (auto i : ideas) {
		if (i.getAct() == 3 && i.getStatus() == "accepted") {
			f << i.getDescription() << " {" << i.getCreator() << "}\n";
		}
	}
	f.close();
}
