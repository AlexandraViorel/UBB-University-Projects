#pragma once
#include <vector>
#include "sourceFile.h"

class SourceFilesRepo {
private:
	std::vector<SourceFile> sourceFiles;
	void loadFile();

public:
	SourceFilesRepo();

	void addSourceFile(SourceFile f);

	void updateSourceFile(std::string name, std::string newStatus, std::string newReviewer);

	void sort();

	std::vector<SourceFile> getFiles();

	std::string getFileCreator(std::string name);
};