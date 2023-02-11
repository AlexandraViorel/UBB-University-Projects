#include "MedicationRepository.h"
#include "stdio.h"
#include "stdlib.h"
#include <string.h>
#include "assert.h"

MedicationRepository* createMedicationRepository(int capacity)
{
    MedicationRepository* medicationRepo = (MedicationRepository*)malloc(sizeof(MedicationRepository));
    if (medicationRepo == NULL) {
        return NULL;
    }

    medicationRepo->medicationsData = createDynamicArray(capacity, destoryMedication, copyMedication);

    return medicationRepo;
}

void destoryMedicationRepository(MedicationRepository* medRepo)
{
    if (medRepo == NULL) {
        return;
    }

    destroyDynamicArray(medRepo->medicationsData);
    free(medRepo);
    medRepo = NULL;
}

int getMedRepoLength(MedicationRepository* medRepo)
{
    return medRepo->medicationsData->length;
}

int findMedication(MedicationRepository* medRepo, char name[], double concentration)
{
    int length = getMedRepoLength(medRepo);
    for (int i = 0; i < length; i++) {
        if (strcmp(getName(medRepo->medicationsData->elements[i]), name) == 0 &&
            getConcentration(medRepo->medicationsData->elements[i]) == concentration) {
            return i;
        }
    }
    return -1;
}

int addMedication(MedicationRepository* medRepo, Medication* med)
{
    int position = findMedication(medRepo, med->name, med->concentration);
    if (position == -1) {
        addElement(medRepo->medicationsData, med);
        return 1;
    }
    else {
        Medication* oldMed = getElementAtIndex(medRepo->medicationsData, position);
        updateMedication(medRepo, med->name, med->concentration, med->quantity + oldMed->quantity, med->price);
        destoryMedication(med);
        return 1;
    }
    return 0;
}


void addTenElements(MedicationRepository* medRepo)
{
    addMedication(medRepo, createMedication("algocalmin", 2, 50, 10.5));
    addMedication(medRepo, createMedication("paracetamol", 5, 35, 8));
    addMedication(medRepo, createMedication("nurofen", 6.5, 80, 15));
    addMedication(medRepo, createMedication("coldrex", 10, 60, 35));
    addMedication(medRepo, createMedication("parasinus", 4, 15, 12.3));
    addMedication(medRepo, createMedication("decasept", 1, 100, 15));
    addMedication(medRepo, createMedication("memoPlus", 3, 70, 24));
    addMedication(medRepo, createMedication("noSpa", 5, 45, 6));
    addMedication(medRepo, createMedication("detrical", 6, 50, 18));
    addMedication(medRepo, createMedication("centrum", 3, 90, 40));
}

int deleteMedication(MedicationRepository* medRepo, char name[], double concentration)
{
    int position = findMedication(medRepo, name, concentration);
    if (position != -1) {
        deleteElement(medRepo->medicationsData, position);
        return 1;
    }
    else {
        return 0;
    }
}

int updateMedication(MedicationRepository* medRepo, char* name, double concentration, int newQuantity, double newPrice)
{
    int count = getArrayLength(medRepo->medicationsData);
    for (int i = 0; i < count; i++)
    {
        Medication* med = getElementAtIndex(medRepo->medicationsData, i);
        if (strcmp(getName(med), name) == 0 && getConcentration(med) == concentration)
        {
            setQuantity(med, newQuantity);
            setPrice(med, newPrice);
            return 1;
        }
    }

    return 0;
}

DynamicArray* getRepoMedications(MedicationRepository* medRepo)
{
    if (medRepo == NULL)
    {
        return NULL;
    }

    return medRepo->medicationsData;
}

MedicationRepository* copyMedRepo(MedicationRepository* medRepo)
{
    MedicationRepository* newMedRepo = createMedicationRepository(medRepo->medicationsData->capacity);
    destroyDynamicArray(newMedRepo->medicationsData);
    newMedRepo->medicationsData = copyDynamicArray(medRepo->medicationsData);
    return newMedRepo;
}

void testMedRepo()
{
    MedicationRepository* medRepo = createMedicationRepository(15);
    Medication* med = createMedication("algocalmin", 23, 10, 8);

    assert(getRepoMedications(medRepo), medRepo->medicationsData);


    addMedication(medRepo, med);
    assert(medRepo->medicationsData->elements[0], med);

    assert(getMedRepoLength(medRepo), 1);

    updateMedication(medRepo, "algocalmin", 23, 100, 100);
    assert(getQuantity(medRepo->medicationsData->elements[0]), 100);
    assert(getPrice(medRepo->medicationsData->elements[0]), 100);

    deleteMedication(medRepo, "algocalmin", 23);
    assert(medRepo->medicationsData->elements, NULL);

    destoryMedicationRepository(medRepo);
    assert(medRepo, NULL);
}
