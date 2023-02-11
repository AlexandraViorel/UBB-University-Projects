#pragma once
#include "Service.h"
#include "Medication.h"

typedef struct {
	Service* service;
} UI;

UI* createUI(Service* service);

void destoryUI(UI* ui);

void printMenu();

int addMedicationUI(UI* ui);

int deleteMedicationUI(UI* ui);

int updateMedicationUI(UI* ui);

void start(UI* ui);