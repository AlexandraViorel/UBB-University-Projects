#pragma once
#include "Service.h"

class UI {
private:
	Service* serv;

public:
	UI(Service* serv);
	void printMenu();

	void removeP();

	void printPatients();

	void quarantinePatients();

	void run();
};