// code_18.cpp
#include <iostream>
#include <random>
using namespace std; // utilisation de l'espace de nom de std

// création du PRNG
default_random_engine dre;

// générateur suivant une loi normale
normal_distribution <double> nd;

// générateur suivant une loi uniforme
uniform_real_distribution <double> urd;

double getGaussian() {
	return nd(dre);
}

// fonction personnalisée -> loi normale
double getUniform() { // fonction personnalisée -> loi uniforme
	return urd(dre);
}

int main() {
	for (int i=0;i<1000;i++){
	cout << getGaussian() << " " << getUniform() << endl;
	}
	return 0;
}