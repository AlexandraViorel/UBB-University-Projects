#pragma once
#include "programmersRepo.h"
#include "sourceFilesRepo.h"
#include "observer.h"

class Service : public Observable {
private:
	ProgrammerRepo& progRepo;
	SourceFilesRepo& filesRepo;

public:
	Service(ProgrammerRepo& p, SourceFilesRepo& f);

	void addFileServ(std::string name, std::string status, std::string creator, std::string reviewer);

	void updateFileServ(std::string name, std::string newStatus, std::string newReviewer);

	void updateProgrammerServ(std::string name);
	
	std::vector<Programmer> getProgrammersServ();
	std::vector<SourceFile> getFilesServ();
	std::vector<SourceFile> getSortedFiles();

	int getProgRevisedServ(std::string name);
	int getProgTotalServ(std::string name);
	std::string getFileCreatorServ(std::string name);

};