// dans cellule.cpp
#include "cellule.h"
#include<iostream>

cellule::cellule(){
	numero=0;
	diametre=0;
}

cellule::cellule(int numero, double diametre){
	this->numero=numero;
	this->diametre=diametre;
}

cellule::~cellule(){
}

int cellule::getNumero()const{
	return numero;
}

double cellule::getDiametre()const{
	return diametre;
}

void cellule::setDiametre(double diametre){
	this->diametre=diametre;
}

cellule cellule::operator+(cellule target){
	return cellule(numero+target.numero, diametre+target.diametre);
}
