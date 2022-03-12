#include <iostream>
#include <string> 
using namespace std;

int main(int argc, char **argv) {
	int a[] = {};
	int choice; int i = 0; int max = -1; int min = 21; float mean;
	do {
		cout << "Saisir la note [0/20] (-1 pour arrêter) : ";
		cin >> choice;
		if (choice < 0) break;
		a[i] = choice; i++;
		if (choice > max) max = choice;
		if (choice < min) min = choice;
		cout << endl;
	} while (true);
	cout << "Nombre de notes : " << i+1 << endl;
	cout << "Note minimale : " << min << endl;
	cout << "Note maximale : " << max << endl;
 	return 0;
}