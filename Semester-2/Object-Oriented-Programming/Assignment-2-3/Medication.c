#include "Medication.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "assert.h"

Medication* createMedication(char* name, double concentration, int quantity, double price)
{
    Medication* medication = malloc(sizeof(Medication));
    if (medication == NULL) {
        return NULL;
    }
    medication->name = (char*)malloc(sizeof(char) * (strlen(name) + 1));
    if (medication->name != NULL) {
        memcpy(medication->name, name, strlen(name) + 1);
    }
    medication->concentration = concentration;
    medication->quantity = quantity;
    medication->price = price;

    return medication;
}

void destoryMedication(Medication* medication)
{
    if (medication == NULL) {
        return;
    }

    free(medication->name);

    free(medication);
    medication = NULL;
}

Medication* copyMedication(Medication* med)
{
    if (med == NULL) {
        return NULL;
    }
    Medication* med1 = createMedication(med->name, med->concentration, med->quantity, med->price);
    return med1;
}

char* getName(Medication* medication)
{
    if (medication == NULL) {
        return NULL;
    }
    return medication->name;
}

double getConcentration(Medication* medication)
{
    if (medication == NULL) {
        return -1;
    }
    return medication->concentration;
}

int getQuantity(Medication* medication)
{
    if (medication == NULL) {
        return -1;
    }
    return medication->quantity;
}

double getPrice(Medication* medication)
{
    if (medication == NULL) {
        return -1;
    }
    return medication->price;
}

void setConcentration(Medication* medication, double newConcentration)
{
    medication->concentration = newConcentration;
}

void setQuantity(Medication* medication, int newQuantity)
{
    medication->quantity = newQuantity;
}

void setPrice(Medication* medication, double newPrice)
{
    medication->price = newPrice;
}

void toString(Medication* medication, char str[])
{
    if (medication == NULL) {
        return;
    }
    sprintf_s(str, "Name: %s; Concentration: %.2lf; Quantity: %d; Price: %.2lf", medication->name,
        medication->concentration, medication->quantity, medication->price);
}

void TestMedication()
{
    Medication* med = createMedication("algocalmin", 23, 10, 8);
    assert(getName(med), "algocalmin");
    assert(getConcentration(med), 23);
    assert(getQuantity(med), 10);
    assert(getPrice(med), 8);
    setConcentration(med, 10);
    assert(getConcentration(med), 10);
    setQuantity(med, 100);
    assert(getQuantity(med), 100);
    setPrice(med, 15);
    assert(getPrice(med), 15);
    destoryMedication(med);
    assert(med, NULL);
}
