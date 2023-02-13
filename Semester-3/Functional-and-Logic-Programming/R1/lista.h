#ifndef LISTA_H
#define LISTA_H


//tip de data generic (pentru moment este intreg)
typedef int TElem;

//referire a structurii Nod;
struct Nod;

//se defineste tipul PNod ca fiind adresa unui Nod
typedef Nod *PNod;

typedef struct Nod{
    TElem e;
	PNod urm;
};

typedef struct{
//prim este adresa primului Nod din lista
	PNod _prim;
} Lista;

//operatii pe lista - INTERFATA

	TElem firstElem(Lista l);

	bool checkEmpty(Lista l);

	Lista listFromSecond(Lista l);

	Lista voidList();

	PNod getLast(Lista l);

	bool equal(Lista l1, Lista l2);

	Lista intersection(Lista l1, Lista l2, Lista rez);

	Lista add(Lista l, TElem e);

//crearea unei liste din valori citite pana la 0
    Lista creare();
//tiparirea elementelor unei liste
    void tipar(Lista l);
// destructorul listei
	void distruge(Lista l);

#endif
