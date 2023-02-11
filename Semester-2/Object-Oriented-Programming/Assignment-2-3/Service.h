#pragma once
#include "MedicationRepository.h"

typedef struct {
	MedicationRepository* medRepository;
	DynamicArray* undoStack;
	int undoPointer;
} Service;

/// <summary>
/// This function creates the service.
/// </summary>
/// <param name="medRepo"></param>
/// <returns> The created service. </returns>
Service* createService(MedicationRepository* medRepo);

/// <summary>
/// This function destroys the service.
/// </summary>
/// <param name="service"></param>
void destroyService(Service* service);

/// <summary>
/// This function gets the medication repository.
/// </summary>
/// <param name="service"></param>
/// <returns> the medication repository </returns>
MedicationRepository* getMedicationRepository(Service* service);

/// <summary>
/// This function creates a medication with the given name, concentration, quantity and price and the it adds it 
/// to the repository.
/// </summary>
/// <param name="service"></param>
/// <param name="name">: the name of the medication to be added </param>
/// <param name="concentration">: the concentration of the medication to be added </param>
/// <param name="quantity">: the quantity of the medication to be added </param>
/// <param name="price">: the price of the medication to be added </param>
/// <returns> 1 if the medication was successfully added, else 0 </returns>
int add(Service* service, char* name, double concentration, int quantity, double price);

/// <summary>
/// This function deletes the medication with the given name and concentration.
/// </summary>
/// <param name="service"></param>
/// <param name="name">: the name of the medication to be deleted </param>
/// <param name="concentration">: the concentration of the medication to be deleted </param>
/// <returns> 1 if the medication was successfully deleted, else 0 </returns>
int deleteMedServ(Service* service, char* name, double concentration);

/// <summary>
/// This function updates the quantity and the price of a medication with given name and concentration.
/// </summary>
/// <param name="service"></param>
/// <param name="name">: the name of the medication to be updated </param>
/// <param name="concentration">: the concentration of the medication to be updated </param>
/// <param name="new_quantity">: the new quantity of the medication</param>
/// <param name="new_price">: the new price of the medication</param>
/// <returns> 1 if the medication was successfully updated, else 0 </returns>
int update(Service* service, char* name, double concentration, int new_quantity, double new_price);

/// <summary>
/// This function gets the medications.
/// </summary>
/// <param name="serv"></param>
/// <returns> The array of medications.</returns>
DynamicArray* getMedications(Service* serv);

/// <summary>
/// This function creates an array with the medications that contain a given string in their name.
/// If the given string is -1 it returns all the medications.
/// </summary>
/// <param name="serv"></param>
/// <param name="name">: the given name </param>
/// <returns> the array of medications with the given string. </returns>
DynamicArray* getMedicationsByName(Service* serv, char* name);

/// <summary>
/// This function creates an array with the medications that are in short supply (their quantity is less than a
/// given quantity).
/// </summary>
/// <param name="serv"></param>
/// <param name="quantity">: the given quantity </param>
/// <returns> the array of medications in short supply. </returns>
DynamicArray* getMedicationsByQuantity(Service* serv, int quantity);

/// <summary>
/// This function creates an array with the medications that have a price smaller than a given price.
/// </summary>
/// <param name="serv"></param>
/// <param name="price">: the given price </param>
/// <returns> the array of medications with the smaller price. </returns>
DynamicArray* getMedicationsByPrice(Service* serv, double price);

/// <summary>
/// This function sorts the array of medications ascending by their name.
/// </summary>
/// <param name="arr">: the array of medications</param>
void sortMedicationsVectorAscendingByName(DynamicArray* arr);

/// <summary>
/// This function sorts the array of medications descending by their name.
/// </summary>
/// <param name="arr">: the array of medications</param>
void sortMedicationsVectorDescendingByName(DynamicArray* arr);

/// <summary>
/// This function undoes the last operation
/// </summary>
/// <returns> 1 if the operation was successfully undone, else 0</returns>
int undo(Service* serv);

/// <summary>
/// This function redoes the last operation
/// </summary>
/// <returns> 1 if the operation was successfully redone, else 0</returns>
int redo(Service* serv);

void testService();