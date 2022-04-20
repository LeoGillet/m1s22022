#include <iostream>

using namespace std;

int factorial(int faxe) {
	if (faxe == 1) return faxe;
	return faxe*factorial(faxe-1);
}

int main() {
	cout << factorial(5) << endl;
	return 0;
}