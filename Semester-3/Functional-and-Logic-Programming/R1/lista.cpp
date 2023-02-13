#include "lista.h"
#include <iostream>
#include <string>

using namespace std;


PNod creare_rec(){
  TElem x;
  cout<<"x=";
  cin>>x;
  if (x==0)
    return NULL;
  else{
    PNod p=new Nod();
    p->e=x;
    p->urm=creare_rec();
    return p;
  }
}

TElem firstElem(Lista l)
{
    return l._prim->e;
}

bool checkEmpty(Lista l)
{
    return l._prim == NULL;
}

Lista listFromSecond(Lista l)
{
    Lista newList;
    newList._prim = l._prim->urm;
    return newList;
}

Lista voidList()
{
    Lista l;
    l._prim = NULL;
    return l;
}

PNod getLast(Lista l)
{
    if (l._prim->urm == NULL)
        return l._prim;
    return getLast(listFromSecond(l));
}

bool equal(Lista l1, Lista l2)
{
    if (l1._prim != NULL && l2._prim != NULL && l1._prim->e != l2._prim->e)
        return false;
    else if (l1._prim == NULL && l2._prim == NULL) {
        return true;
    }
    else if (l1._prim == NULL || l2._prim == NULL) {
        return false;
    }
    else {
        l1._prim = l1._prim->urm;
        l2._prim = l2._prim->urm;
        equal(l1, l2);
    }
}

Lista intersection(Lista l1, Lista l2, Lista rez)
{
    if (l1._prim == NULL || l2._prim == NULL) {
        return rez;
    }
    else if (l1._prim->e == l2._prim->e) {
        add(rez, l1._prim->e);
        //std::cout << std::to_string(l1._prim->e);
        l1._prim = l1._prim->urm;
        intersection(l1, l2, rez);
    }
    else if (l1._prim->e != l2._prim->e && l2._prim->urm != NULL) {
        l2._prim = l2._prim->urm;
        intersection(l1, l2, rez);
    }
    else if (l2._prim == NULL && l1._prim != NULL) {
        l1._prim = l1._prim->urm;
        intersection(l1, l2, rez);
    }
}

Lista add(Lista l, TElem e)
{
    PNod p = new Nod();
    p->e = e;
    p->urm = l._prim;
    l._prim = p;
    return l;
}

Lista creare(){
   Lista l;
   l._prim=creare_rec();
   return l;
}

void tipar_rec(PNod p){
   if (p!=NULL){
     cout<<p->e<<" ";
     tipar_rec(p->urm);
   }
}

void tipar(Lista l){
   tipar_rec(l._prim);
}

void distrug_rec(PNod p){
   if (p!=NULL){
     distrug_rec(p->urm);
     delete p;
   }
}

void distruge(Lista l) {
	//se elibereaza memoria alocata nodurilor listei
    distrug_rec(l._prim);
}

