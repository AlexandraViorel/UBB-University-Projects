#pragma once
#include "Medication.h"
#include "DynamicArray.h"
#include <stdlib.h>

typedef struct {
	DynamicArray* medicationsData;
} MedicationRepository;

/// <summary>
/// This function creates a medication repository with the given capacity.
/// </summary>
/// <param name="capacity"></param>
/// <returns> The created repository. </returns>
MedicationRepository* createMedicationRepository(int capacity);

/// <summary>
/// This function destroys the given medication repository.
/// </summary>
/// <param name="medRepo"></param>
void destoryMedicationRepository(MedicationRepository* medRepo);

/// <summary>
/// This function gets the length of the medication repository.
/// </summary>
/// <param name="medRepo"></param>
/// <returns> The length. </returns>
int getMedRepoLength(MedicationRepository* medRepo);

/// <summary>
/// This function searches if a medication with the given name and concentration exists in the repository.
/// </summary>
/// <param name="medRepo"></param>
/// <param name="name"></param>
/// <param name="concentration"></param>
/// <returns> the position if it exists, else -1 </returns>
int findMedication(MedicationRepository* medRepo, char name[], double concentration);

/// <summary>
/// This function adds a medication to the repository.
/// </summary>
/// <param name="medRepo"></param>
/// <param name="med"></param>
/// <returns> 1 if the medication was successfully added, else 0 </returns>
int addMedication(MedicationRepository* medRepo, Medication* med);

/// <summary>
/// This function adds 10 medications to the repository.
/// </summary>
/// <param name="medRepo"></param>
void addTenElements(MedicationRepository* medRepo);

/// <summary>
/// This function deletes a medication with the given name and concentration from the repository.
/// </summary>
/// <param name="medRepo"></param>
/// <param name="name"></param>
/// <param name="concentration"></param>
/// <returns> 1 if the medication was successfully deleted, else 0 </returns>
int deleteMedication(MedicationRepository* medRepo, char name[], double concentration);

/// <summary>
/// This function updates a medication with the given name and concentration.
/// </summary>
/// <param name="medRepo"></param>
/// <param name="name"></param>
/// <param name="concentration"></param>
/// <param name="newQuantity"></param>
/// <param name="newPrice"></param>
/// <returns> 1 if the medication was successfully updated, else 0 </returns>
int updateMedication(MedicationRepository* medRepo, char* name, double concentration, int newQuantity, double newPrice);

/// <summary>
/// This function gets the data from the medication repository.
/// </summary>
/// <param name="medRepo"></param>
/// <returns></returns>
DynamicArray* getRepoMedications(MedicationRepository* medRepo);

MedicationRepository* copyMedRepo(MedicationRepository* medRepo);

void testMedRepo();