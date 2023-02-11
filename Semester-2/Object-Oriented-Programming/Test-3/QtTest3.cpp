#include "QtTest3.h"
#include <QMessageBox>
#include <cmath>

QtTest3::QtTest3(Service& s, QWidget *parent)
    : serv{ s }, QMainWindow(parent)
{
    ui.setupUi(this);

    populateList();
    connections();
}

void QtTest3::populateList()
{
    this->ui.eqListWidget->clear();
    std::vector<Equation> allEqus = this->serv.getData();
    for (Equation e : allEqus)
    {
        if (e.getDet() > 0)
        {
            QString eqString = QString::fromStdString(e.toString());
            QListWidgetItem* item = new QListWidgetItem{ eqString };
            item->setBackground(Qt::green);
            this->ui.eqListWidget->addItem(item);
        }
        else {
            QString eqString = QString::fromStdString(e.toString());
            QListWidgetItem* item = new QListWidgetItem{ eqString };
            this->ui.eqListWidget->addItem(item);
        }
    }
}

void QtTest3::connections()
{
    QWidget::connect(this->ui.addButton, &QPushButton::clicked, this, &QtTest3::addEq);

    QWidget::connect(this->ui.computeButton, &QPushButton::clicked, this, &QtTest3::computeSols);
}

int QtTest3::getSelectedIndex()
{

    QModelIndexList selectedIndexes = this->ui.eqListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.size() == 0)
    {
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void QtTest3::addEq()
{
    if (this->ui.aLineEdit->text().isEmpty() || this->ui.bLineEdit->text().isEmpty() || this->ui.cLineEdit->text().isEmpty()) {
        QMessageBox::critical(this, "Error", "Please input all the numbers!");
        this->ui.aLineEdit->clear();
        this->ui.bLineEdit->clear();
        this->ui.cLineEdit->clear();
        return;
    }
    double a = this->ui.aLineEdit->text().toDouble();
    double b = this->ui.bLineEdit->text().toDouble();
    double c = this->ui.cLineEdit->text().toDouble();
    if (a == 0) {
        QMessageBox::critical(this, "Error", "a cannot be 0!");
        this->ui.aLineEdit->clear();
        this->ui.bLineEdit->clear();
        this->ui.cLineEdit->clear();
        return;
    }
    else {
        this->serv.addServ(a, b, c);
    }
    this->populateList();
    this->ui.aLineEdit->clear();
    this->ui.bLineEdit->clear();
    this->ui.cLineEdit->clear();
}

void QtTest3::computeSols()
{
    int index = this->getSelectedIndex();
    if (index < 0) {
        QMessageBox::critical(this, "Error", "Please select a equation!");
        return;
    }
    std::vector<Equation> equs = this->serv.getData();
    Equation eq = equs[index];
    double det = eq.getDet();
    if (det < 0) {
        double b = eq.getB() * (-1);
        double s = b / (2 * eq.getA());
        double d = sqrt(abs(det)) / (2 * eq.getA());
        std::string sol1 = std::to_string(s) + "+" + std::to_string(d) + "*i";
        std::string sol2 = std::to_string(s) + "-" + std::to_string(d) + "*i";
        this->ui.sol1lineEdit->clear();
        this->ui.sol2lineEdit->clear();
        this->ui.sol1lineEdit->setText(QString::fromStdString(sol1));
        this->ui.sol2lineEdit->setText(QString::fromStdString(sol2));
    }
    else {
        double b = eq.getB() * (-1);
        double s1 = (b + sqrt(det)) / (2 * eq.getA());
        double s2 = (b - sqrt(det)) / (2 * eq.getA());
        std::string sol1 = std::to_string(s1);
        std::string sol2 = std::to_string(s2);
        this->ui.sol1lineEdit->clear();
        this->ui.sol2lineEdit->clear();
        this->ui.sol1lineEdit->setText(QString::fromStdString(sol1));
        this->ui.sol2lineEdit->setText(QString::fromStdString(sol2));
    }
}
