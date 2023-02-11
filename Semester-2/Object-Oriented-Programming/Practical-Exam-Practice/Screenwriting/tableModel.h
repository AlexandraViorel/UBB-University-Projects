#pragma once
#include <QAbstractTableModel>
#include "repository.h"

class WriterTableModel : public QAbstractTableModel
{
private:
    Repository& repo;

public:
    WriterTableModel(Repository& r);

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;

    int columnCount(const QModelIndex& parent = QModelIndex()) const override;

    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;

    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;

    void addIdea(const Idea& i);

    void updateIdea(Idea& i);

    void clearData();

};