#pragma once
#include "Service.h"

class UI {
private:
	Service& serv;
public:
	UI(Service& s);
	void printMenu();
	void handleAdd();
	void handleListAll();
	void handleListAlert();
	void run();
};