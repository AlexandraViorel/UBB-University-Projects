#pragma once

#include <QWidget>
#include "ui_WriterWindow.h"
#include "repository.h"
#include <QTableView>
#include "tableModel.h"
#include "DevelopWindow.h"

class WriterWindow : public QWidget
{
	Q_OBJECT

public:
	WriterWindow(Writer writer, Repository& repo, WriterTableModel* model, QWidget *parent = Q_NULLPTR);
	~WriterWindow();

private:
	Ui::WriterWindow ui;
	Writer writer;
	Repository& repo;
	WriterTableModel* model;

	void initialize();
	void connections();
	void handleAddIdea();
	int getSelectedIndex() const;
	void handleAcceptIdea();
	void handleDevelop();
	void handleSavePlot();
};
