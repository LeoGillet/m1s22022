#include <iostream>

using namespace std;

int ask(string prompt) {
	int choice;
	cout << prompt;
	cin >> choice;
	return choice;
}

int main() {
	int n = 0; int somme = 0;
	int entier = ask("Saisir un entier : ");
	while (somme < entier) {
		somme += ++n;
	}
	cout << "Valeur de n = " << n-1 << " avec une somme de : " << somme-n << endl;
	return 0;
}