// code_34.cpp
#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<math.h>
using namespace std; // utilisation de l'espace de nom de std

int main(){
	double C0=10.0;double k=0.3;int nPoints=24;int dt=1;
	double C=C0;
	vector<double> time,Ct,Cte;
	// calcul des valeurs "exactes" dans Cte
	for (int i=0;i<nPoints;i++){
		time.push_back((double)i);
		Cte.push_back(C0*exp(-k*(double)i));
	}
	// calcul estimé avec la méthode d'Euler
	for (int i=0;i<nPoints;i++){
		Ct.push_back(C);
		C=C+dt*(-k*C);
	}
	// création de la variable data de type string pour écriture
	string data="time Cte Ct\n";
	for (int i=0;i<nPoints;i++){
		data+=to_string(time[i])+" "+to_string(Cte[i])+" "+to_string(Ct[i])+"\n";
	}
	// ouverture en écriture du fichier
	ofstream fichier("test_34.txt");
	if(fichier){
		fichier << data;
		fichier.close();
	} else cerr << "Impossible d'ouvrir le fichier !" << endl;
    return 0;
}
