#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(int argc, char **argv) {
	map<string,int> rels;
	int choice; int i = 0; int max = -1; int min = 21; float mean; string name;
	string max_n; string min_n;
	do {
		cout << "Saisir le nom (stop pour arrêter) : ";
		cin >> name;
		if (name == "stop") break;
		cout << "Saisir la note [0/20] : ";
		cin >> choice;
		rels[name] = choice; i++;
		if (choice > max) {max = choice; max_n = name;}
		if (choice < min) {min = choice; min_n = name;}
		cout << endl;
	} while (true);
	cout << "Nombre de notes : " << i << endl;
	cout << "Note minimale : " << min << " (" << min_n << ")" << endl;
	cout << "Note maximale : " << max << " (" << max_n << ")"<< endl;
 	return 0;
}