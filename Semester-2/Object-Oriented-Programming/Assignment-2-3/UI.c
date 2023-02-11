#include "UI.h"
#include "stdio.h"
#include "stdlib.h"
#include <crtdbg.h>

UI* createUI(Service* service)
{
    UI* ui = malloc(sizeof(UI));
    if (ui == NULL) {
        return NULL;
    }
    ui->service = service;
    return ui;
}

void destoryUI(UI* ui)
{
    if (ui == NULL) {
        return;
    }
    destroyService(ui->service);
    free(ui);
}

void printMenu()
{
    printf("---- OPTIONS MENU ----\n");
    printf("0 : exit \n");
    printf("1 : add medication \n");
    printf("2 : delete medication \n");
    printf("3 : update medication \n");
    printf("4 : print medications by name\n");
    printf("5 : filter medications \n");
    printf("6 : undo \n");
    printf("7 : redo \n");
}

int readIntegerNumber(char* message)
{
    char string[16] = { 0 };
    int result;
    int flag = 0;
    int read;

    while (flag == 0) {
        printf(message);
        scanf_s("%15s", &string, 15);
        read = sscanf_s(string, "%d", &result);
        flag = (read == 1);

        if (flag == 0) {
            printf("Invalid option!\n");
        }
    }
    return result;
}

int addMedicationUI(UI* ui)
{
    char name[50];
    double concentration = 0, price = 0;
    int quantity = 0;

    printf("Please input the name of the medication: ");

    scanf_s("%49s", &name, 49);

    printf("Please input the concentration: ");

    if (1 != scanf_s("%lf", &concentration))
    {
        while (getchar() != '\n');
        return 0;
    }

    printf("Please input the quantity: ");
    if (1 != scanf_s("%d", &quantity))
    {
        while (getchar() != '\n');
        return 0;
    }

    printf("Please input the price: ");
    if (1 != scanf_s("%lf", &price))
    {
        while (getchar() != '\n');
        return 0;
    }

    return add(ui->service, name, concentration, quantity, price);
}

int deleteMedicationUI(UI* ui)
{
    char name[50];
    double concentration = 0;

    printf("Please input the name of the medication you want to delete: ");
    scanf_s("%s", &name, 15);
    printf("Please input the concentration of the medication you want to delete: ");
    scanf_s("%lf", &concentration);
    return deleteMedServ(ui->service, name, concentration);
    return 0;
}

int updateMedicationUI(UI* ui)
{
    char name[50];
    double concentration = 0, new_price = 0;
    int new_quantity = 0;

    printf("Please input the name of the medication you want to update: ");
    scanf_s("%s", &name, 49);
    printf("Please input the concentration of the medication you want to update: ");
    scanf_s("%lf", &concentration);
    printf("Please input the new quantity of the medication you want to update: ");
    scanf_s("%d", &new_quantity);
    printf("Please input the new price of the medication you want to update: ");
    scanf_s("%lf", &new_price);

    return update(ui->service, name, concentration, new_quantity, new_price);
}

void printVector(DynamicArray* vec)
{
    if (vec == NULL)
    {
        return;
    }

    int count = getArrayLength(vec);
    for (int i = 0; i < count; i++)
    {
        Medication* med = getElementAtIndex(vec, i);
        if (med != NULL)
        {
            char* name = getName(med);
            double concentration = getConcentration(med);
            int quantity = getQuantity(med);
            double price = getPrice(med);
            printf("Name:%s | Concentration:%lf | Quantity:%d | Price:%lf\n", name, concentration, quantity, price);
        }
    }
}

int chooseSortType() {
    int option;
    printf("How do you want to sort the medications ? \n");
    printf("1 : ascending \n");
    printf("2 : descending \n");
    printf("Please input your option: ");
    scanf_s("%d", &option);
    return option;
}

void printMedicationsByName(UI* ui)
{
    char name[50];
    printf("Please input the string to search for: ");
    scanf_s("%s", &name, 49);

    if (strcmp(name, "-1") == 0)
    {
        DynamicArray* medData = getMedications(ui->service);
        while (1)
        {
            int sortOption = chooseSortType();
            if (sortOption == 1) {
                sortMedicationsVectorAscendingByName(medData);
                break;
            }
            else if (sortOption == 2) {
                sortMedicationsVectorDescendingByName(medData);
                break;
            }
            else {
                printf("Invalid option for sorting, try again !");
            }
        }
        printVector(medData);
    }
    else
    {
        DynamicArray* meds = getMedicationsByName(ui->service, name);
        while (1)
        {
            int sortOption = chooseSortType();
            if (sortOption == 1) {
                sortMedicationsVectorAscendingByName(meds);
                break;
            }
            else if (sortOption == 2) {
                sortMedicationsVectorDescendingByName(meds);
                break;
            }
            else {
                printf("Invalid option for sorting, try again !");
            }
        }
        printVector(meds);
        destroyDynamicArray(meds);
    }
}

int chooseFilterType()
{
    int option;
    printf("How do you want to filter the medications ? \n");
    printf("1 : by quantity \n");
    printf("2 : by price \n");
    printf("Please input your option: \n");
    scanf_s("%d", &option);
    return option;
}

void printMedicationsBySomething(UI* ui)
{
    while (1)
    {
        int option = chooseFilterType();
        if (option == 1)
        {
            int quantity;
            printf("Please input the quantity to search for : ");
            scanf_s("%d", &quantity);
            DynamicArray* meds = getMedicationsByQuantity(ui->service, quantity);
            printVector(meds);
            break;
        }
        else if (option == 2)
        {
            double price;
            printf("Please input the price to search for: ");
            scanf_s("%lf", &price);
            DynamicArray* meds = getMedicationsByPrice(ui->service, price);
            printVector(meds);
            break;
        }
        else
        {
            printf("Invalid option for filter ! Try again !");
        }
    }
}

int undoUI(UI* ui)
{
    return undo(ui->service);
}

int redoUI(UI* ui)
{
    return redo(ui->service);
}

void start(UI* ui)
{
    while (1) {
        printMenu();
        int option = readIntegerNumber("Please choose your option: ");
        if (option == 0) 
        {
            return;
        }
        else if (option == 1) 
        {
            int addResult = addMedicationUI(ui);
            if (addResult == 1) 
            {
                printf("Medication successfully added ! \n");
            }
            else 
            {
                printf("Medication cannot be added ! \n");
            }
        }
        else if (option == 2) 
        {
            int deleteResult = deleteMedicationUI(ui);
            if (deleteResult == 1) 
            {
                printf("Medication successfully deleted ! \n");
            }
            else 
            {
                printf("Medication cannot be deleted ! \n");
            }
        }
        else if (option == 3) 
        {
            int updateResult = updateMedicationUI(ui);
            if (updateResult == 1) 
            {
                printf("Medication successfully updated ! \n");
            }
            else 
            {
                printf("Medication cannot be updated ! \n");
            }
        }
        else if (option == 4)
        {
            printMedicationsByName(ui);
        }
        else if (option == 5)
        {
            printMedicationsBySomething(ui);
        }
        else if (option == 6)
        {
            int undoResult = undoUI(ui);
            if (undoResult == 1)
            {
                printf("Operation successfully undone ! \n");
            }
            else
            {
                printf("Operation cannot be undone ! \n");
            }
        }
        else if (option == 7)
        {
            int redoResult = redoUI(ui);
            if (redoResult == 1)
            {
                printf("Operation successfully redone ! \n");
            }
            else
            {
                printf("Operation cannot be redone ! \n");
            }
        }
        else if (option < 0 || option > 7)
        {
            printf("Invalid option ! Try again !");
        }

    }
}

void tests() 
{
    TestMedication();
    testMedRepo();
    testService();
    testDynamicArray();
}

int main() {
    MedicationRepository* medRepo = createMedicationRepository(30);
    Service* service = createService(medRepo);
    UI* ui = createUI(service);

    start(ui);

    destoryUI(ui);

    tests();
    _CrtDumpMemoryLeaks();
}