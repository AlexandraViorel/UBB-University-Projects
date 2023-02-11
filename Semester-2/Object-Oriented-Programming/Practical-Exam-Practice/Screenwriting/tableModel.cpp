#include "tableModel.h"

WriterTableModel::WriterTableModel(Repository& r) : repo{ r }
{
}

int WriterTableModel::rowCount(const QModelIndex& parent) const
{
    return this->repo.getIdeas().size();
}

int WriterTableModel::columnCount(const QModelIndex& parent) const
{
    return 4;
}

QVariant WriterTableModel::data(const QModelIndex& index, int role) const
{
    int row = index.row();
    int column = index.column();

    Idea i = this->repo.getIdeas()[row];

    if (role == Qt::DisplayRole)
    {
        switch (column)
        {
        case 0:
            return QString::fromStdString(i.getDescription());
        case 1:
            return QString::fromStdString(i.getStatus());
        case 2:
            return QString::fromStdString(i.getCreator());
        case 3:
            return QString::fromStdString(std::to_string(i.getAct()));
        default:
            break;
        }

    }

    return QVariant();
}

QVariant WriterTableModel::headerData(int section, Qt::Orientation orientation, int role) const
{
    if (orientation == Qt::Horizontal)
    {
        if (role == Qt::DisplayRole)
        {
            switch (section)
            {
            case 0:
                return QString{ "Description" };
            case 1:
                return QString{ "Status" };
            case 2:
                return QString{ "Creator" };
            case 3:
                return QString{ "Act" };
            default:
                break;
            }
        }
    }


    return QVariant();
}

void WriterTableModel::addIdea(const Idea& i)
{
    int n = this->repo.getIdeas().size();
    this->beginInsertRows(QModelIndex{}, n, n);
    this->repo.addIdeaRepo(i);
    this->endInsertRows();
}

void WriterTableModel::updateIdea(Idea& i)
{
    this->repo.updateIdeaRepo(i);
}

void WriterTableModel::clearData()
{

}