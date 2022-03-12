#include <iostream>
#include <string> 
using namespace std;

int factorial(int x) {
	if (x == 1) return x;
    return x*factorial(x-1);
}

int main(int argc, char** argv) {
	if (argc > 1) {
		int arg = stoi(argv[1]);
		cout << "factorial(" << arg << ") \t";
		cout << factorial(arg) << endl;
	}
	return 0;
}