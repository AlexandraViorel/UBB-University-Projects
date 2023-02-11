#include "Matrix.h"
#include <exception>
using namespace std;


Matrix::Matrix(int nrLines, int nrCols) 
{
	if ((nrLines <= 0) || (nrCols <= 0))
	{
		throw exception();
	}
	this->nColumns = nrCols;
	this->nLines = nrLines;
	this->nrElements = 0;
	this->capacity = 20; // this is the capacity for the arrays
	this->CRowArrLength = nrLines + 1;
	this->values = new TElem[capacity];
	this->ColumnArr = new int[capacity];
	this->CRowArr = new int[CRowArrLength];

	for (int i = 0; i < this->CRowArrLength; i++)
	{
		this->CRowArr[i] = 0;
	}

}


// Complexity: Teta(1)
int Matrix::nrLines() const 
{
	return this->nLines;
}

// Complexity: Teta(1)
int Matrix::nrColumns() const 
{
	return this->nColumns;
}

// Complexity: O(n)
// Best case: Teta(1) if it throws an exception or the element is the first
// Worst case: O(n) if the element does not exist
TElem Matrix::element(int i, int j) const
{
	if ((i >= nLines) || (j >= nColumns) || (i < 0) || (j < 0))
	{
		throw exception();
	}
	for (int position = this->CRowArr[i]; position < this->CRowArr[i + 1]; position++)
	{
		if (this->ColumnArr[position] == j)
		{
			return values[position];
		}
	}
	return NULL_TELEM;
}

// Complexity: O(n)
// Best case: Teta(1) if it throws an exception
// Worst case: O(n) if every column contains an element
int Matrix::numberOfNonZeroElems(int line) const
{
	if (line < 0 || line >= this->nLines)
	{
		throw exception();
	}
	int k = 0;
	for (int j = 0; j < this->nColumns; j++)
	{
		TElem el = element(line, j);
		if (el != NULL_TELEM)
		{
			k++;
		}
	}
	return k;
}


// Complexity: Teta(n)
void Matrix::resize(const char* message)
{
	int* newColumnArr;
	TElem* newValues;

	if (message == "g")
	{
		this->capacity *= 2;
	} 
	else
	{
		this->capacity /= 2;
	}

	newColumnArr = new int[capacity];
	newValues = new TElem[capacity];

	for (int i = 0; i < nrElements; i++)
	{
		newColumnArr[i] = this->ColumnArr[i];
		newValues[i] = this->values[i];
	}
	this->ColumnArr = newColumnArr;
	this->values = newValues;
}

// Complexity: O(n)
// Best case: O(1) if the last element must be removed
// Worst case: O(n) if the first element must be removed
void Matrix::remove(int line, int column, int index)
{
	for (int pos = index + 1; pos < nrElements; pos++) 
	{
		ColumnArr[pos - 1] = ColumnArr[pos];
		values[pos - 1] = values[pos];
	}

	nrElements--;

	for (int pos = line + 1; pos < CRowArrLength; pos++)
	{
		CRowArr[pos]--;
	}
}

// Complexity: O(n)
// Best case: O(1) if the element must be inserted at the end of the array
// Worst case: O(n) if the element must be inserted at the beginning of the array
void Matrix::insert(int line, int column, int index, TElem element)
{
	this->nrElements++;
	for (int position = nrElements; position > index; position--)
	{
		ColumnArr[position] = ColumnArr[position - 1];
		values[position] = values[position - 1];
	}
	ColumnArr[index] = column;
	values[index] = element;
	for (int position = line + 1; position < CRowArrLength; position++)
	{
		CRowArr[position]++;
	}
}

// Complexity: O(n)
// Best case: O(1) if it throws an exception
// Worst case: O(n)
TElem Matrix::modify(int i, int j, TElem e) 
{
	if (i < 0 || j < 0 || i >= this->nLines || j >= this->nColumns)
	{
		throw exception();
	}
	TElem el;
	int position = CRowArr[i];
	int column = -1;
	for (position; position < this->CRowArr[i + 1]; position++)
	{
		column = ColumnArr[position];
		if (column >= j)
		{
			break;
		}

	}
	if (column != j)
	{
		if (e != 0)
		{
			if (this->nrElements == this->capacity)
			{
				resize("g");
			}
		
			int index = CRowArr[i];
			while (ColumnArr[index] < j && index < CRowArr[i + 1])
			{
				index++;
			}
			el = values[index];
			insert(i, j, index, e);
			return el;
		}
	}
	else
	{
		if (e != 0)
		{
			el = values[position];
			this->values[position] = e;
			return el;
		}
		else
		{
			int index = this->CRowArr[i];
			while (ColumnArr[index] < j && index < CRowArr[i + 1])
			{
				index++;
			}
			if (nrElements == this->capacity / 4)
			{
				resize("l");
			}
			el = values[position];
			remove(i, j, index);
			return el;
		}
	}
	return NULL_TELEM;
}
