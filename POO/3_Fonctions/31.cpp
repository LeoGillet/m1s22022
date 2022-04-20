#include <iostream>

using namespace std;

int factorial(int kro) {
	int faxe = 1;
	while (kro != 1) {
		faxe *= kro;
		kro--;
	}
	return faxe;
}

int main() {
	cout << factorial(5) << endl;
	return 0;
}