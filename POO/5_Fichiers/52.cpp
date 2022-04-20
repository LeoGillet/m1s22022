#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string read_data(string filename) {
	ifstream fichier(filename);
	string text; string line;

	if (fichier) {
		while(getline(fichier, line)) {
			text += line+"\n";
		}
		fichier.close();
	} else {cout << "Erreur" << endl;}
	return text;
}

int main() {
	cout << read_data("data_01.txt") << endl;
	return 0;
}