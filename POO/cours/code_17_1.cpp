// code_17_1.cpp
#include <iostream>
#include <vector>
using namespace std; // utilisation de l'espace de nom de std
void f1(int val){val=val*3;}
void f2(int& val){val=val*3;}
void f3(vector<int> vec){vec[0]=vec[0]*3;}
void f4(vector<int>& vec){vec[0]=vec[0]*3;}

// test_17_1.cpp suite et fin ...
int main(){
	int valeur_1=10;
	cout << "valeur_1 initiale : " << valeur_1 << endl;
	f1(valeur_1);
	cout << "valeur_1 apres f1 : " << valeur_1 << endl; // inchangé
	f2(valeur_1);
	cout << "valeur_1 apres f2 : " << valeur_1 << endl; // changé
	vector<int> vecteur_1={10};
	cout << "vecteur_1[0] initial : " << vecteur_1[0] << endl;
	f3(vecteur_1);
	cout << "vecteur_1[0] apres f3 : " << vecteur_1[0] << endl; // inchangé
	f4(vecteur_1);
	cout << "vecteur_1[0] apres f4 : " << vecteur_1[0] << endl; // changé
	return 0;
}