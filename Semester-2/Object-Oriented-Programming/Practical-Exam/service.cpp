#include "service.h"

Service::Service(ProgrammerRepo& p, SourceFilesRepo& f) : progRepo{ p }, filesRepo{ f }
{
}

void Service::addFileServ(std::string name, std::string status, std::string creator, std::string reviewer)
{
	SourceFile f{ name, status, creator, reviewer };
	this->filesRepo.addSourceFile(f);
}

void Service::updateFileServ(std::string name, std::string newStatus, std::string newReviewer)
{
	this->filesRepo.updateSourceFile(name, newStatus, newReviewer);
}

void Service::updateProgrammerServ(std::string name)
{
	this->progRepo.updateProgrammer(name);
}

std::vector<Programmer> Service::getProgrammersServ()
{
	return this->progRepo.getProgrammers();
}

std::vector<SourceFile> Service::getFilesServ()
{
	return this->filesRepo.getFiles();
}

std::vector<SourceFile> Service::getSortedFiles()
{
	this->filesRepo.sort();
	return this->filesRepo.getFiles();
}

int Service::getProgRevisedServ(std::string name)
{
	return this->progRepo.getProgRevised(name);
}

int Service::getProgTotalServ(std::string name)
{
	return this->progRepo.getProgTotal(name);
}

std::string Service::getFileCreatorServ(std::string name)
{
	return this->filesRepo.getFileCreator(name);
}
