#include <iostream>
#include <typeinfo>
using namespace std;
int main(void){
	int a[]={65,76,65,66,65,77,65};
	char b[]={65,108,97,98,97,109,97};
	cout << char(a[0]) << char(a[1]) << char (a[2]) << char(a[3]) << char(a[4])
	<< char(a[5]) << char(a[6]) << endl;
	cout << b << endl;
	return 0;
}