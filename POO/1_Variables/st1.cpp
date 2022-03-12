#include <iostream>
using namespace std;

/* a + b
 * +: opérateur
 * a, b: opérandes */

int main(void) {
	short aShort = 1;
	int aInt = 2;
	float aFloat = 1.75;
	double aDouble = 2.75;
	cout << "(aShort) Type: " <<typeid(aShort).name() << " : " << aShort << endl;
	cout << "(aInt) Type: " <<typeid(aInt).name() << " : " << aInt << endl;
	cout << "(aFloat) Type: " <<typeid(aFloat).name() << " : " << aFloat << endl;
	cout << "(aDouble) Type: " <<typeid(aDouble).name() << " : " << aDouble << endl;
	cout << "(aDouble * aShort) Type: " <<typeid(aDouble*aShort).name() << " : " << aDouble*aShort << endl;
	aShort = aShort * aDouble;
	cout << "(aShort = aShort * aDouble) Type: " <<typeid(aShort).name() << " : " << aShort << endl;
}

