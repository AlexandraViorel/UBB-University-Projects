//#pragma once
//#include <qwidget.h>
//#include "domain.h"
//#include "service.h"
//#include "repository.h"
//#include <qlabel.h>
//#include <qlistwidget.h>
//#include <qformlayout.h>
//#include <qlineedit.h>
//#include <qtextedit.h>
//#include <qpushbutton.h>
//
//class GUI : public QWidget {
//	
//	Q_OBJECT
//
//public:
//	GUI(Service& s, Repository& r, QWidget* parent = 0);
//	~GUI();
//
//private:
//	Service& serv;
//	Repository& repo;
//	std::vector<Dog> dogs;
//
//	QListWidget* dogsList;
//	QListWidget* adoptionList;
//	QLineEdit* nameEdit;
//	QLineEdit* breedEdit;
//	QLineEdit* ageEdit;
//	QLineEdit* photoLinkEdit;
//	QLineEdit* filterEdit;
//	QPushButton* addDogButton;
//	QPushButton* deleteDogButton;
//	QPushButton* updateDogButton;
//	QPushButton* adoptButton;
//	QPushButton* showPhotoButton;
//	QPushButton* nextButton;
//
//	void initializeGUI();
//	void populateDogsList(std::string filterText);
//	void filterFunction();
//	void connectToDogs();
//};