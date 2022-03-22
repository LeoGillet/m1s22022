#include <iostream>
#include <random>
#include <map>
using namespace std; 

default_random_engine dre;
uniform_real_distribution <double> urd;

int secret_value() {
	cout << urd(dre);
	return 1+(10-1)*urd(dre);
}



int main() {
	cout << secret_value() << endl;
	return 0;
}