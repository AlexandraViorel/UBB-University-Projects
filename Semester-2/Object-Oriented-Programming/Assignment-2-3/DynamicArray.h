#pragma once
#include "Medication.h"

typedef void* TElem;
typedef void (*DestroyElementFunction)(void*);
typedef TElem (*CopyElementFunction)(TElem);

typedef struct DynamicArray {
	TElem* elements;
	int length;
	int capacity;
	DestroyElementFunction destroyFunction;
	CopyElementFunction copyFunction;
} DynamicArray;

/// <summary>
/// This function creates a dynamic array with generic items and a given capacity.
/// </summary>
/// <param name="capacity">: integer, maximum capacity of the dynamic array. </param>
/// <param name="destroyFunction">: pointer to a destroy function, used to destroy the elements from the dynamic array. </param>
/// <returns> a pointer to the created dynamic array  </returns>
DynamicArray* createDynamicArray(int capacity, DestroyElementFunction destroyFunction, CopyElementFunction copyFunction);

/// <summary>
/// This function destroys a dynamic array.
/// </summary>
/// <param name="arr">: the dynamic array to be destoryed. </param>
void destroyDynamicArray(DynamicArray* arr);

/// <summary>
/// This function adds an element to the dynamic array.
/// </summary>
/// <param name="arr">: the dynamic array </param>
/// <param name="element">: the element to be added </param>
void addElement(DynamicArray* arr, TElem element);

/// <summary>
/// This function deletes an element from a given position.
/// </summary>
/// <param name="arr">: the dynamic array</param>
/// <param name="position">: the position from which the element will be deleted </param>
void deleteElement(DynamicArray* arr, int position);

/// <summary>
/// This function gets the element with a given index.
/// </summary>
/// <param name="arr">: the dynamic array</param>
/// <param name="index">: the given index</param>
/// <returns> the element found on the given index </returns>
void* getElementAtIndex(DynamicArray* arr, int index);

/// <summary>
/// This function gets the length of the dynamic array.
/// </summary>
/// <param name="arr">: the dynamic array</param>
/// <returns> the length of the dynamic array </returns>
int getArrayLength(DynamicArray* arr);

/// <summary>
/// This function gets the elements of the array.
/// </summary>
/// <param name="arr"></param>
/// <returns></returns>
TElem* getArrayElements(DynamicArray* arr);

/// <summary>
/// This function creates a copy for a given dynamic array.
/// </summary>
/// <param name="arr">: the dynamic array for which a copy will be created</param>
/// <returns> the copy of </returns>
DynamicArray* copyDynamicArray(DynamicArray* arr);

void testDynamicArray();