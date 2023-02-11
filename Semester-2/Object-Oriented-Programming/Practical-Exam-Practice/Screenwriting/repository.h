#pragma once
#include <vector>
#include "writer.h"
#include "idea.h"

class Repository {
private:
	std::vector<Writer> writers;
	std::vector<Idea> ideas;
	void loadWriters();
	void loadIdeas();

public:
	Repository();
	void addIdeaRepo(Idea i);
	void updateIdeaRepo(Idea id);
	void saveIdeasToFile(std::string filename);
	void savePlot(std::string filename);

	std::vector<Idea> getIdeas();
	std::vector<Writer> getWriters();

	std::vector<Idea> getAcceptedIdeas(Writer w);
};