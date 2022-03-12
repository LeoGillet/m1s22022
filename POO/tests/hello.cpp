#include <iostream>
using namespace std;

int main(int argc, char** argv) {
	cout << argc << endl;
	for (unsigned int i=0;i<argc;i++) { // parcours tous les éléments par indice
		cout << argv[i] << endl;
	}
	return 0; 
}