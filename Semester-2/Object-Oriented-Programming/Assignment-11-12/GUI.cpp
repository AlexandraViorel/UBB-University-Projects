//#include "GUI.h"
//
//GUI::GUI(Service& s, Repository& r, QWidget* parent) : serv{s}, repo{r}
//{
//	this->initializeGUI();
//	this->populateDogsList("");
//	this->connectToDogs();
//}
//
//GUI::~GUI()
//{
//}
//
//void GUI::initializeGUI()
//{
//	// The general layout of the window.
//	QHBoxLayout* layout = new QHBoxLayout{ this };
//
//	// We choose a font and size
//	QFont f{ "Verdana", 10 };
//
//	// A. The left side of the window
//	QWidget* leftSide = new QWidget{};
//	QVBoxLayout* leftLayout = new QVBoxLayout{ leftSide };
//
//	// 1. The list of dogs
//	this->dogsList = new QListWidget{};
//	this->dogsList->setSelectionMode(QAbstractItemView::SingleSelection);
//	QLabel* allDogsLabel = new QLabel{ "All dogs" };
//	allDogsLabel->setFont(f);
//
//	// We add the list to the left layout
//	leftLayout->addWidget(allDogsLabel);
//	leftLayout->addWidget(this->dogsList);
//
//	// 2. Dog data line edits
//	QWidget* formLayout = new QWidget{};
//	QFormLayout* dogLayout = new QFormLayout{ formLayout };
//
//	this->nameEdit = new QLineEdit{};
//	this->breedEdit = new QLineEdit{};
//	this->ageEdit = new QLineEdit{};
//	this->photoLinkEdit = new QLineEdit{};
//	this->filterEdit = new QLineEdit{};
//
//	// Name label & line edit
//	QLabel* nameLabel = new QLabel{ "&Name:" };
//	nameLabel->setBuddy(this->nameEdit);
//	nameLabel->setFont(f);
//	this->nameEdit->setFont(f);
//
//	// Breed label & line edit
//	QLabel* breedLabel = new QLabel{ "&Breed:" };
//	breedLabel->setBuddy(this->breedEdit);
//	breedLabel->setFont(f);
//	this->breedEdit->setFont(f);
//
//	// Age label & line edit
//	QLabel* ageLabel = new QLabel{ "&Age:" };
//	ageLabel->setBuddy(this->ageEdit);
//	ageLabel->setFont(f);
//	this->ageEdit->setFont(f);
//
//	// Photography link label & line edit
//	QLabel* photoLabel = new QLabel{ "&Photography link:" };
//	photoLabel->setBuddy(this->photoLinkEdit);
//	photoLabel->setFont(f);
//	this->photoLinkEdit->setFont(f);
//
//	// Filter label & line edit
//	QLabel* filterLabel = new QLabel{ "&Filter:" };
//	filterLabel->setBuddy(this->filterEdit);
//	filterLabel->setFont(f);
//	this->filterEdit->setFont(f);
//
//	// We add all of them to the dog layout
//	dogLayout->addRow(nameLabel, this->nameEdit);
//	dogLayout->addRow(breedLabel, this->breedEdit);
//	dogLayout->addRow(ageLabel, this->ageEdit);
//	dogLayout->addRow(photoLabel, this->photoLinkEdit);
//	dogLayout->addRow(filterLabel, this->filterEdit);
//
//	// We add it to the left layout
//	leftLayout->addWidget(formLayout);
//
//	// 3. Buttons of the left side
//	QWidget* buttonsWidget = new QWidget{};
//	QGridLayout* gridLayout = new QGridLayout{ buttonsWidget };
//
//	// Add button
//	this->addDogButton = new QPushButton("Add");
//	this->addDogButton->setFont(f);
//
//	// Delete button
//	this->deleteDogButton = new QPushButton("Delete");
//	this->deleteDogButton->setFont(f);
//
//	// Update button
//	this->updateDogButton = new QPushButton("Update");
//	this->updateDogButton->setFont(f);
//
//	// We add all of them to the buttons layout
//	gridLayout->addWidget(this->addDogButton, 0, 0);
//	gridLayout->addWidget(this->deleteDogButton, 0, 1);
//	gridLayout->addWidget(this->updateDogButton, 0, 2);
//
//	// We add the buttons to the left layout
//	leftLayout->addWidget(buttonsWidget);
//
//	// B. The middle side of the window
//	QWidget* middleSide = new QWidget{};
//	QVBoxLayout* middleLayout = new QVBoxLayout{ middleSide };
//
//	// Adopt button
//	this->adoptButton = new QPushButton(">");
//	this->adoptButton->setFont(f);
//
//	// We add the button to the middle layout
//	middleLayout->addWidget(this->adoptButton);
//
//	// C. The right side of the window
//	QWidget* rightSide = new QWidget{};
//	QVBoxLayout* rightLayout = new QVBoxLayout{ rightSide };
//
//	// 1. The adoption list
//	this->adoptionList = new QListWidget{};
//	this->adoptionList->setSelectionMode(QAbstractItemView::SingleSelection);
//	QLabel* adoptionLabel = new QLabel{ "Adoption list" };
//	adoptionLabel->setFont(f);
//
//	// We add the adoption list to the right layout
//	rightLayout->addWidget(adoptionLabel);
//	rightLayout->addWidget(this->adoptionList);
//
//	// 2. Adoption buttons
//	QWidget* buttonsAdoption = new QWidget{};
//	QGridLayout* gridAdoption = new QGridLayout{ buttonsAdoption };
//
//	// Show photography button
//	this->showPhotoButton = new QPushButton("Show photography");
//	this->showPhotoButton->setFont(f);
//
//	// Next button
//	this->nextButton = new QPushButton("Next");
//	this->nextButton->setFont(f);
//
//	gridAdoption->addWidget(this->showPhotoButton, 0, 0);
//	gridAdoption->addWidget(this->nextButton, 0, 1);
//
//	// We add the buttons to the right layout
//	rightLayout->addWidget(buttonsAdoption);
//
//	// We add all layouts to the general layout
//	layout->addWidget(leftSide);
//	layout->addWidget(middleSide);
//	layout->addWidget(rightSide);
//}
//
//void GUI::populateDogsList(std::string filterText)
//{
//	this->dogsList->clear();
//	std::vector<Dog> allDogs = this->serv.getDogsList();
//	for (auto d : allDogs) {
//		if (d.getName().find(filterText) != d.getName().npos)
//		{
//			QString dogString = QString::fromStdString(d.toString());
//			QListWidgetItem* item = new QListWidgetItem{ dogString };
//			this->dogsList->addItem(item);
//		}
//	}
//}
//
//void GUI::filterFunction()
//{
//	std::string filterText = this->filterEdit->text().toStdString();
//	this->populateDogsList(filterText);
//}
//
//void GUI::connectToDogs()
//{
//	QObject::connect(this->filterEdit, &QLineEdit::textChanged, this, &GUI::filterFunction);
//}
