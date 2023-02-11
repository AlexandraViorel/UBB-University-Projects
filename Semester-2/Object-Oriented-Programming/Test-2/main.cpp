#include "ui.h"

int main() {
	Service serv(true);
	UI ui(serv);
	ui.run();
}