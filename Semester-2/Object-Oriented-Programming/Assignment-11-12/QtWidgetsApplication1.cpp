#include "QtWidgetsApplication1.h"
#include <qmessagebox.h>
#include <QtCharts/QChartView>
#include <QtCharts/QPieSeries>
//#include <QtCharts/QBarCategoryAxis>
//#include <QtCharts/QBarSeries>
//#include <QtCharts/QBarSet>
//#include <QtCharts/QValueAxis>
#include "errors.h"

QtWidgetsApplication1::QtWidgetsApplication1(Service& s, UserService& u, QWidget *parent)
    : QMainWindow(parent), serv{ s }, userServ{ u }
{
	this->userRepoTypeSelected = false;

    ui.setupUi(this);

	populateDogsList("");

	populateDogsListUser("", 1000);

	connectSignalsAndSlots();
}

void QtWidgetsApplication1::connectSignalsAndSlots()
{
	QObject::connect(this->ui.dogsListWidget, &QListWidget::itemSelectionChanged, [this]() {
		int selectedIndex = getSelectedIndex();
		if (selectedIndex < 0) {
			return;
		}
		Dog d = serv.getDogsList()[selectedIndex];
		ui.nameLineEdit->setText(QString::fromStdString(d.getName()));
		ui.breedLineEdit->setText(QString::fromStdString(d.getBreed()));
		ui.ageLineEdit->setText(QString::fromStdString(std::to_string(d.getAge())));
		ui.photoLineEdit->setText(QString::fromStdString(d.getPhotoLink()));

	});

	QObject::connect(this->ui.dogsListWidgetUser, &QListWidget::itemSelectionChanged, [this]() {
		int selectedIndex = getSelectedIndexUser();
		if (selectedIndex < 0) {
			return;
		}
		Dog d = serv.getDogsList()[selectedIndex];
		ui.nameLineEditUser->setText(QString::fromStdString(d.getName()));
		ui.breedLineEditUser->setText(QString::fromStdString(d.getBreed()));
		ui.ageLineEditUser->setText(QString::fromStdString(std::to_string(d.getAge())));
		ui.photoLineEditUser->setText(QString::fromStdString(d.getPhotoLink()));

		});
	QObject::connect(this->ui.deleteButton, &QPushButton::clicked, this, &QtWidgetsApplication1::deleteDog);
	QObject::connect(this->ui.addButton, &QPushButton::clicked, this, &QtWidgetsApplication1::addDog);
	QObject::connect(this->ui.updateButton, &QPushButton::clicked, this, &QtWidgetsApplication1::updateDog);
	QObject::connect(this->ui.filterLineEdit, &QLineEdit::textChanged, this, &QtWidgetsApplication1::filterDogs);

	if (userRepoTypeSelected == false) {
		QObject::connect(this->ui.CSVradioButton, &QRadioButton::clicked, [this]() {
			userServ.chooseRepositoryType(1);
			userRepoTypeSelected = true;
			});
	}

	if (userRepoTypeSelected == false) {
		QObject::connect(this->ui.HTMLradioButton, &QRadioButton::clicked, [this]() {
			userServ.chooseRepositoryType(2);
			userRepoTypeSelected = true;
			});
	}

	QObject::connect(this->ui.adoptButton, &QPushButton::clicked, this, &QtWidgetsApplication1::adoptDog);
	QObject::connect(this->ui.filterNameUserLineEdit, &QLineEdit::textChanged, this, &QtWidgetsApplication1::filterDogsUser);
	QObject::connect(this->ui.filterAgeUserLineEdit, &QLineEdit::textChanged, this, &QtWidgetsApplication1::filterDogsUser);

	QObject::connect(this->ui.openFileButton, &QPushButton::clicked, [this]() {
		if (!userRepoTypeSelected) {
			QMessageBox::critical(this, "Error", "Please select the type of the file !");
			return;
		}
		else {
			std::string link = std::string("start ").append(userServ.getFileName());
			system(link.c_str());
		}
	});

	QObject::connect(this->ui.chartButton, &QPushButton::clicked, this, &QtWidgetsApplication1::makeCharts);
}

int QtWidgetsApplication1::getSelectedIndex() const
{
	QModelIndexList selectedIndexes = this->ui.dogsListWidget->selectionModel()->selectedIndexes();
	if (selectedIndexes.size() == 0) {
		this->ui.nameLineEdit->clear();
		this->ui.breedLineEdit->clear();
		this->ui.ageLineEdit->clear();
		this->ui.photoLineEdit->clear();
		return -1;
	}

	int selectedIndex = selectedIndexes.at(0).row();
	return selectedIndex;
}

void QtWidgetsApplication1::populateDogsList(std::string filterText)
{
	this->ui.dogsListWidget->clear();
	std::vector<Dog> allDogs = this->serv.getDogsList();
	for (auto d : allDogs) {
		if (d.getName().find(filterText) != d.getName().npos)
		{
			QString dogString = QString::fromStdString(d.toString());
			QListWidgetItem* item = new QListWidgetItem{ dogString };
			this->ui.dogsListWidget->addItem(item);
		}
	}
}

void QtWidgetsApplication1::addDog()
{
	try
	{
		std::string name = this->ui.nameLineEdit->text().toStdString();
		std::string breed = this->ui.breedLineEdit->text().toStdString();
		std::string ageStr = this->ui.ageLineEdit->text().toStdString();
		int age = std::stoi(ageStr);
		std::string photographyLink = this->ui.photoLineEdit->text().toStdString();

		this->serv.addDogServ(name, breed, age, photographyLink);

		this->populateDogsList("");
		this->populateDogsListUser("", 1000);

		int lastElement = this->serv.getDogsList().size() - 1;
		this->ui.dogsListWidget->setCurrentRow(lastElement);
	}
	catch (RepoError)
	{
		QMessageBox::critical(this, "Error", "A dog with the same name already exists !");
		return;
	}

}

void QtWidgetsApplication1::deleteDog()
{
	int selectedIndex = this->getSelectedIndex();
	if (selectedIndex < 0) {
		QMessageBox::critical(this, "Error", "No dog was selected !");
		return;
	}

	Dog d = this->serv.getDogsList()[selectedIndex];
	this->serv.removeDogServ(d.getName());

	this->populateDogsList("");
	this->populateDogsListUser("", 1000);

}

void QtWidgetsApplication1::updateDog()
{
	int index = this->getSelectedIndex();
	if (index < 0) {
		QMessageBox::critical(this, "Error", "No dog was selected !");
		return;
	}
	try {
		std::string oldName = this->serv.getDogsList()[index].getName();
		std::string newBreed = this->ui.breedLineEdit->text().toStdString();
		std::string newAgeStr = this->ui.ageLineEdit->text().toStdString();
		int newAge = stoi(newAgeStr);
		std::string newPhoto = this->ui.photoLineEdit->text().toStdString();
		this->serv.updateDogServ(oldName, newBreed, newAge, newPhoto);
		this->populateDogsList("");
		this->populateDogsListUser("", 1000);
	}
	catch (RepoError) 
	{
		QMessageBox::critical(this, "Error", "Error at updating dog !");
		return;
	}
}

void QtWidgetsApplication1::filterDogs()
{
	std::string filterText = this->ui.filterLineEdit->text().toStdString();
	this->populateDogsList(filterText);
}

int QtWidgetsApplication1::getSelectedIndexUser() const
{
	QModelIndexList selectedIndexes = this->ui.dogsListWidgetUser->selectionModel()->selectedIndexes();
	if (selectedIndexes.size() == 0) {
		this->ui.nameLineEditUser->clear();
		this->ui.breedLineEditUser->clear();
		this->ui.ageLineEditUser->clear();
		this->ui.photoLineEditUser->clear();
		return -1;
	}


	int selectedIndex = selectedIndexes.at(0).row();
	return selectedIndex;
}

void QtWidgetsApplication1::populateDogsListUser(std::string filterText, int ageFilter)

{
	this->ui.dogsListWidgetUser->clear();
	std::vector<Dog> allDogs = this->serv.getDogsList();
	for (auto d : allDogs) {
		if (d.getName().find(filterText) != d.getName().npos && d.getAge() < ageFilter)
		{
			QString dogString = QString::fromStdString(d.toString());
			QListWidgetItem* item = new QListWidgetItem{ dogString };
			this->ui.dogsListWidgetUser->addItem(item);
		}
	}
}

void QtWidgetsApplication1::filterDogsUser()
{
	std::string filterText = this->ui.filterNameUserLineEdit->text().toStdString();
	std::string ageStr = this->ui.filterAgeUserLineEdit->text().toStdString();
	int filterAge = 1000;
	if (ageStr != "") {
		filterAge = stoi(ageStr);
	}
	this->populateDogsListUser(filterText, filterAge);
}

void QtWidgetsApplication1::populateAdoptingList()
{
	this->ui.adoptList->clear();
	std::vector<Dog> adoptedDogs = this->userServ.getAdoptingList();
	for (auto d : adoptedDogs) {
		QString dogString = QString::fromStdString(d.toString());
		QListWidgetItem* item = new QListWidgetItem{ dogString };
		this->ui.adoptList->addItem(item);
	}
}

void QtWidgetsApplication1::adoptDog()
{
	int selectedIndex = this->getSelectedIndexUser();
	if (selectedIndex < 0) {
		QMessageBox::critical(this, "Error", "No dog was selected !");
		return;
	}
	try {
		if (!this->userRepoTypeSelected) {
			QMessageBox::critical(this, "Error", "Please select the file type !");
			return;
		}
		std::string name = this->ui.nameLineEditUser->text().toStdString();
		std::string breed = this->ui.breedLineEditUser->text().toStdString();
		std::string ageStr = this->ui.ageLineEditUser->text().toStdString();
		int age = stoi(ageStr);
		std::string photoLink = this->ui.photoLineEditUser->text().toStdString();
		this->userServ.addDogUserServ(name, breed, age, photoLink);
		this->populateAdoptingList();
	}
	catch (RepoError) {
		QMessageBox::critical(this, "Error", "A dog with the same name is already adopted !");
		return;
	}
}

void QtWidgetsApplication1::makeCharts()
{
	/*this->chartWindow = new QWidget{};
	auto* chartLayout = new QVBoxLayout(this->chartWindow);*/
	/*std::vector<std::string> breeds = this->serv.getAllBreeds();

	auto* chart = new QChart();
	auto* axisX = new QBarCategoryAxis();
	axisX->setTitleText("Breeds");

	QStringList categories;
	for (int i = 1; i <= breeds.size(); i++) {
		categories << QString::fromStdString(std::to_string(i));
	}

	axisX->append(categories);
	chart->addAxis(axisX, Qt::AlignBottom);

	auto* axisY = new QValueAxis();
	chart->addAxis(axisY, Qt::AlignLeft);
	axisY->setRange(0, 8);
	axisY->setTitleText("Number of dogs");

	for (std::string& b : breeds) {
		auto* series = new QBarSeries();
		auto* set = new QBarSet(QString::fromStdString(b));
		int nbOfDogs = this->serv.getNbOfDogsWithGivenBreed(b);
		*set << nbOfDogs;
		series->append(set);
		chart->addSeries(series);
		series->attachAxis(axisY);
	}

	chart->setTitle("Number of dogs per breed");
	chart->setAnimationOptions(QChart::SeriesAnimations);

	chart->legend()->setVisible(true);
	chart->legend()->setAlignment(Qt::AlignLeft);

	auto* chartView = new QChartView(chart);
	chartView->setRenderHint(QPainter::Antialiasing);

	chartLayout->addWidget(chartView);*/
	std::vector<std::string> breeds = this->serv.getAllBreeds();

	auto* chart = new QChart();
	auto* pieSeries = new QPieSeries();
	for (auto breed : breeds) {
		int currentNrOfDogs = this->serv.getNbOfDogsWithGivenBreed(breed);
		pieSeries->append(QString::fromStdString(breed + ":" + std::to_string(currentNrOfDogs)), currentNrOfDogs);
	}
	chart->addSeries(pieSeries);
	chart->legend()->setAlignment(Qt::AlignBottom);
	auto* chartView = new QChartView{};
	chartView->setChart(chart);

	auto* chartLayout = new QVBoxLayout{};
	auto* chartWidget = new QWidget{};
	chartLayout->addWidget(chartView);
	chartWidget->setLayout(chartLayout);
	chartWidget->show();

}


