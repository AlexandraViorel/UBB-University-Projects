#include "programmer.h"

Programmer::Programmer(std::string n, int r, int t) : name{ n }, noRevisedFiles{ r }, totalFilesToRevise{ t }
{
}

std::string Programmer::getName()
{
    return this->name;
}

int Programmer::getNoRevisedFiles()
{
    return this->noRevisedFiles;
}

int Programmer::getTotalFilesToRevise()
{
    return this->totalFilesToRevise;
}

void Programmer::setRevisedFiles(int newRev)
{
    this->noRevisedFiles = newRev;
}

void Programmer::setTotalFiles(int newTot)
{
    this->totalFilesToRevise = newTot;
}
