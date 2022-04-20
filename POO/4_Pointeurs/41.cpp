#include <iostream>
using namespace std;

int change_pas(int a) {
	a *= 3;
	return a;
}

int change(int& a) {
	a *= 3;
	return a;
}

int main(void){
	int a=12;
	cout << "change_pas(a) renvoie " << change_pas(a) << " mais : a = " << a <<
	endl;
	cout << "change(a) renvoie " << change(a) << " mais : a = " << a << endl;
	return 0;
}