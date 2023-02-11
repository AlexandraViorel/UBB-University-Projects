#pragma once

template <typename D>
class DynamicArray {
private:
	int capacity;
	int length;
	D* elems;

public:

	DynamicArray(int capacity = 20);

	DynamicArray(const DynamicArray<D>& arr);

	DynamicArray<D>& operator=(const DynamicArray<D>& arr);

	D& operator[](int index);

	void resize();

	void addElement(D element);

	void deleteElement(int position);

	D* elementsGetter();

	int capacityGetter() const;

	int lengthGetter() const;

	~DynamicArray();

};

template<typename D>
DynamicArray<D>::DynamicArray(int capacity)
{
	this->capacity = capacity;
	this->length = 0;
	this->elems = new D[capacity];
}

template<typename D>
DynamicArray<D>::DynamicArray(const DynamicArray<D>& arr)
{
	this->capacity = arr.capacity;
	this->length = arr.length;
	this->elems = new D[this->capacity];

	for (int i = 0; i < arr.length; i++)
	{
		this->elems[i] = arr.elems[i];
	}
}

template<typename D>
DynamicArray<D>& DynamicArray<D>::operator=(const DynamicArray<D>& arr)
{
	if (this == &arr)
	{
		return *this;
	}

	this->length = arr.length;
	this->capacity = arr.capacity;

	delete[] this->elems;
	
	this->elems = new D[this->capacity];
	for (int i = 0; i < this->length; i++)
	{
		this->elems[i] = arr.elems[i];
	}

	return *this;
}

template<typename D>
D& DynamicArray<D>::operator[](int index)
{
	return this->elems[index];		
}

template<typename D>
void DynamicArray<D>::resize()
{
	this->capacity *= 2;
	D* newElems = new D[this->capacity];
	for (int i = 0; i < this->length; i++)
	{
		newElems[i] = this->elems[i];
	}
	delete[] this->elems;
	this->elems = newElems;
}

template<typename D>
void DynamicArray<D>::addElement(D element)
{
	if (this->length == this->capacity)
	{
		this->resize();
	}
	this->elems[this->length++] = element;
}

template<typename D>
void DynamicArray<D>::deleteElement(int position)
{
	if (position < 0 || position >= this->length)
	{
		return;
	}

	for (int i = position; i < this->length - 1; i++)
	{
		this->elems[i] = this->elems[i + 1];
	}
	this->length--;
}

template<typename D>
D* DynamicArray<D>::elementsGetter()
{
	return this->elems;
}

template<typename D>
int DynamicArray<D>::capacityGetter() const
{
	return this->capacity;
}

template<typename D>
int DynamicArray<D>::lengthGetter() const
{
	return this->length;
}

template<typename D>
DynamicArray<D>::~DynamicArray()
{
	delete[] this->elems;
}