// dans cellule.h
#ifndef CELLULE_H
#define CELLULE_H
class cellule {
public:
	cellule();
	cellule(int numero, double diametre);
	~cellule();
	int getNumero()const;
	double getDiametre()const;
	void setDiametre(double diametre);
	cellule operator+(cellule target);
	private:
	int numero;
	double diametre;
};
#endif
