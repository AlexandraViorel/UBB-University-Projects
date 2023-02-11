#pragma once

typedef struct
{
	char* name;
	double concentration;
	int quantity;
	double price;
} Medication;

/// <summary>
/// This function creates a medication.
/// </summary>
/// <param name="name"></param>
/// <param name="concentration"></param>
/// <param name="quantity"></param>
/// <param name="price"></param>
/// <returns></returns>
Medication* createMedication(char* name, double concentration, int quantity, double price);

/// <summary>
/// This function destorys a medication.
/// </summary>
/// <param name="medication"></param>
void destoryMedication(Medication* medication);

Medication* copyMedication(Medication* med);

/// <summary>
/// This function gets the name of a medication.
/// </summary>
/// <param name="medication"></param>
/// <returns> The name of the medication.</returns>
char* getName(Medication* medication);

/// <summary>
/// This function gets the concentration of a medication.
/// </summary>
/// <param name="medication"></param>
/// <returns> The concentration of the medication. </returns>
double getConcentration(Medication* medication);

/// <summary>
/// This function gets the quantity of a medication.
/// </summary>
/// <param name="medication"></param>
/// <returns> The quantity of the medication. </returns>
int getQuantity(Medication* medication);

/// <summary>
/// This function gets the price of a medication.
/// </summary>
/// <param name="medication"></param>
/// <returns> The price of the medication. </returns>
double getPrice(Medication* medication);

/// <summary>
/// This function sets the concentration of a given medication.
/// </summary>
/// <param name="medication"></param>
/// <param name="newConcentration"></param>
void setConcentration(Medication* medication, double newConcentration);

/// <summary>
/// This function sets the quantity of a given medication.
/// </summary>
/// <param name="medication"></param>
/// <param name="newQuantity"></param>
void setQuantity(Medication* medication, int newQuantity);

/// <summary>
/// This function sets the price of a given medication.
/// </summary>
/// <param name="medication"></param>
/// <param name="newPrice"></param>
void setPrice(Medication* medication, double newPrice);

void toString(Medication* medication, char str[]);

void TestMedication();