// code_18.cpp
#include <iostream>
#include <random>
#include <map>
using namespace std; // utilisation de l'espace de nom de std

// création du PRNG
default_random_engine dre;

// générateur suivant une loi normale
normal_distribution <double> nd;

// générateur suivant une loi uniforme
uniform_real_distribution <double> urd;

double getGaussian(double mean, double sd) {
	return mean+nd(dre)*sd;
}

// fonction personnalisée -> loi normale
double getUniform(double min, double max) { // fonction personnalisée -> loi uniforme
	return min+(max-min)*urd(dre);
}

map<string, int> dist_choice() {
	int choice; int rep; map<string,int> ret;
	double val1; double val2;
	cout << "1. Distribution Gaussienne" << endl << "2. Distribution Uniforme" << endl;
	cout << endl << "? > ";
	cin >> choice;
	cout << endl;

	cout << "Nombre de répétitions : ";
	cin >> rep;
	cout << endl;

	if (choice == 1) {
		cout << "Moyenne : ";
		cin >> val1;
		cout << endl << "Ecart-Type : ";
		cin >> val2;
		cout << endl;
	} else {
		cout << "Valeur minimale : ";
		cin >> val1;
		cout << endl << "Valeur maximale : ";
		cin >> val2;
		cout << endl;
	}

	ret["dist"] = choice; ret["reps"] = rep; ret["val1"] = val1; ret["val2"] = val2;
	return ret;
}

int main() {
	map<string, int> arg = dist_choice();
	if (arg["dist"] == 1) {
		vector<double> values;
		for (int i=0; i<arg["reps"] ;i++){
			double value = getGaussian(arg["val1"], arg["val2"]);
			values.push_back(value);
			cout << values.at(i) << endl;
		}
	} else {
		vector<double> values;
		for (int i=0;i<arg["reps"];i++){
			double value = getUniform(arg["val1"], arg["val2"]);
			values.push_back(value);
			cout << values.at(i) << endl;
		}
	}
	return 0;
}