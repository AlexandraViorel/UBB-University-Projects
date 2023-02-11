#include "repository.h"
#include <fstream>
#include <sstream>

void Repository::loadWriters()
{
	std::ifstream f("writers.txt");
	std::string line;
	std::string name, expertise;
	while (std::getline(f, line)) 
	{
		std::istringstream s(line);
		std::getline(s, name, ',');
		std::getline(s, expertise, ',');
		this->writers.push_back(Writer{ name, expertise });
	}
	f.close();
}

void Repository::loadIdeas()
{
	std::ifstream f("ideas.txt");
	std::string line;
	std::string desc, status, creator, actStr;
	while (std::getline(f, line)) {
		std::istringstream s(line);
		std::getline(s, desc, ',');
		std::getline(s, status, ',');
		std::getline(s, creator, ',');
		std::getline(s, actStr, ',');
		this->ideas.push_back(Idea{ desc, status, creator, std::stoi(actStr) });
	}
	f.close();
}

Repository::Repository()
{
	this->loadWriters();
	this->loadIdeas();
}

void Repository::addIdeaRepo(Idea i)
{
	for (auto idea : this->ideas) {
		if (idea.getDescription() == i.getDescription() && idea.getAct() == i.getAct()) {
			throw std::exception("Idea already exists!");
		}
	}
	this->ideas.push_back(i);
}

void Repository::updateIdeaRepo(Idea id)
{
	int k = 0;
	for (auto i : this->ideas)
	{
		if (i.getDescription() == id.getDescription() && i.getAct() == id.getAct()) {
			Idea idea = Idea{ i.getDescription(), "accepted", i.getCreator(), i.getAct() };
			this->ideas.at(k) = idea;
			return;
		}
		k++;
	}
}

void Repository::saveIdeasToFile(std::string filename)
{

}

void Repository::savePlot(std::string filename)
{
}

std::vector<Idea> Repository::getIdeas()
{
	return this->ideas;
}

std::vector<Writer> Repository::getWriters()
{
	return this->writers;
}

std::vector<Idea> Repository::getAcceptedIdeas(Writer w)
{
	std::vector<Idea> result;
	for (auto i : ideas) {
		if (i.getStatus() == "accepted" && i.getCreator() == w.getName())
			result.push_back(i);
	}
	return result;
}
