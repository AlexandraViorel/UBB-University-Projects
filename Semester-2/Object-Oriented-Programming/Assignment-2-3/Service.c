#include "Service.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "assert.h"

Service* createService(MedicationRepository* medRepo)
{
    Service* service = (Service*)malloc(sizeof(Service));
    if (service == NULL) {
        return NULL;
    }
    service->medRepository = medRepo;
    addTenElements(service->medRepository);
    service->undoStack = createDynamicArray(10, destoryMedicationRepository, copyMedRepo);
    addElement(service->undoStack, copyMedRepo(service->medRepository));
    service->undoPointer = -1;
    return service;
}

void destroyService(Service* service)
{
    if (service == NULL) {
        return;
    }
    destoryMedicationRepository(service->medRepository);
    destroyDynamicArray(service->undoStack);
    free(service);
    service = NULL;
}

MedicationRepository* getMedicationRepository(Service* service)
{
    return service->medRepository;
}

void correctUndoPointer(Service* serv)
{
    while (getArrayLength(serv->undoStack) - 2 != serv->undoPointer)
        deleteElement(serv->undoStack, getArrayLength(serv->undoStack) - 1);
}

void addToUndoList(Service* serv)
{
    correctUndoPointer(serv);
    addElement(serv->undoStack, copyMedRepo(serv->medRepository));
    serv->undoPointer++;
}

int add(Service* service, char* name, double concentration, int quantity, double price)
{
    Medication* medication = createMedication(name, concentration, quantity, price);
    int returnValue = addMedication(service->medRepository, medication);
    if (returnValue == 1)
    {
        addToUndoList(service);
    }
    return returnValue;
}

int deleteMedServ(Service* service, char* name, double concentration)
{
    int returnValue = deleteMedication(service->medRepository, name, concentration);
    if (returnValue == 1)
    {
        addToUndoList(service);
    }
    return returnValue;
}

int update(Service* service, char* name, double concentration, int new_quantity, double new_price)
{
    int returnValue = updateMedication(service->medRepository, name, concentration, new_quantity, new_price);
    if (returnValue == 1)
    {
        addToUndoList(service);
    }
    return returnValue;
}

DynamicArray* getMedications(Service* serv)
{
    if (serv == NULL)
    {
        return NULL;
    }

    return getRepoMedications(serv->medRepository);
}

DynamicArray* getMedicationsByPrice(Service* serv, double price)
{
    if (serv == NULL || price < 0) {
        return NULL;
    }

    DynamicArray* meds = getMedications(serv);
    DynamicArray* result = createDynamicArray(meds->capacity, destoryMedication, copyMedication);

    int count = getArrayLength(meds);
    for (int i = 0; i < count; i++)
    {
        Medication* med = getElementAtIndex(meds, i);
        if (med->price < price) {
            Medication* copyMed = createMedication(getName(med), getConcentration(med), getQuantity(med), getPrice(med));
            addElement(result, copyMed);
        }
    }
    return result;
}

void sortMedicationsVectorAscendingByName(DynamicArray* arr)
{
    if (arr == NULL)
    {
        return;
    }

    int ok = 0;
    do {
        ok = 1;
        for (int i = 1; i < arr->length; i++)
        {
            if (strcmp(getName(arr->elements[i]), getName(arr->elements[i - 1])) < 0)
            {
                ok = 0;
                void* tmp = arr->elements[i];
                arr->elements[i] = arr->elements[i - 1];
                arr->elements[i - 1] = tmp;
            }
        }
    } while (!ok);
}

void sortMedicationsVectorDescendingByName(DynamicArray* arr)
{
    if (arr == NULL)
    {
        return;
    }

    int ok = 0;
    do {
        ok = 1;
        for (int i = 1; i < arr->length; i++)
        {
            if (strcmp(getName(arr->elements[i]), getName(arr->elements[i - 1])) > 0)
            {
                ok = 0;
                void* tmp = arr->elements[i];
                arr->elements[i] = arr->elements[i - 1];
                arr->elements[i - 1] = tmp;
            }
        }
    } while (!ok);
}

int undo(Service* serv)
{
    int undoStackLength = getArrayLength(serv->undoStack);
    if (undoStackLength <= 1 || serv->undoPointer < 0)
    {
        return 0;
    }
    else
    {
        destoryMedicationRepository(serv->medRepository);
        serv->medRepository = copyMedRepo(getElementAtIndex(serv->undoStack, serv->undoPointer));
        serv->undoPointer--;
        return 1;
    }
}

int redo(Service* serv)
{
    int undoStackLength = getArrayLength(serv->undoStack);
    if (serv->undoPointer == undoStackLength - 2 || serv->undoPointer < -1)
    {
        return 0;
    }
    else
    {
        destoryMedicationRepository(serv->medRepository);
        serv->medRepository = copyMedRepo(getElementAtIndex(serv->undoStack, serv->undoPointer + 2));
        serv->undoPointer++;
        return 1;
    }
}

DynamicArray* getMedicationsByName(Service* serv, char* name)
{
    if (serv == NULL || name == NULL)
    {
        return NULL;
    }

    DynamicArray* meds = getMedications(serv);
    DynamicArray* result = createDynamicArray(meds->capacity, destoryMedication, copyMedication);

    int count = getArrayLength(meds);
    for (int i = 0; i < count; i++)
    {
        Medication* med = getElementAtIndex(meds, i);
        if (strstr(getName(med), name))
        {
            Medication* copyMed = createMedication(getName(med), getConcentration(med), getQuantity(med), getPrice(med));
            addElement(result, copyMed);
        }
    }
    return result;
}

DynamicArray* getMedicationsByQuantity(Service* serv, int quantity)
{
    if (serv == NULL || quantity < 0) {
        return NULL;
    }

    DynamicArray* meds = getMedications(serv);
    DynamicArray* result = createDynamicArray(meds->capacity, destoryMedication, copyMedication);

    int count = getArrayLength(meds);
    for (int i = 0; i < count; i++) 
    {
        Medication* med = getElementAtIndex(meds, i);
        if (med->quantity < quantity) {
            Medication* copyMed = createMedication(getName(med), getConcentration(med), getQuantity(med), getPrice(med));
            addElement(result, copyMed);
        }
    }
    return result;
}



void testService()
{
    MedicationRepository* medRepo = createMedicationRepository(15);
    Service* serv = createService(medRepo);

    add(serv, "abcd", 23, 10, 8);
    assert(getMedRepoLength(serv->medRepository), 11);

    update(serv, "abcd", 23, 100, 100);
    assert(getQuantity(serv->medRepository->medicationsData->elements[10]), 100);
    assert(getPrice(medRepo->medicationsData->elements[10]), 100);

    DynamicArray* medsByName = getMedicationsByName(serv, "abcd");
    assert(medsByName->length, 1);
    destroyDynamicArray(medsByName);

    DynamicArray* medsByQuantity = getMedicationsByQuantity(serv, 101);
    assert(medsByQuantity->length, 1);
    destroyDynamicArray(medsByQuantity);

    DynamicArray* medsByPrice = getMedicationsByPrice(serv, 500);
    assert(medsByPrice->length, 11);
    destroyDynamicArray(medsByPrice);

    deleteMedServ(serv, "algocalmin", 23);
    assert(serv->medRepository->medicationsData->elements, NULL);

    undo(serv);
    assert(serv->medRepository->medicationsData->length, 11);

    redo(serv);
    assert(serv->medRepository->medicationsData->elements, NULL);

    destroyService(serv);
    assert(serv, NULL);
}