#include <iostream>
#include <typeinfo>
using namespace std;

int main(void){
	int i1=0;int i2=1;
	short s1=1;
	float f1=2.75;
	double d1=2.75;
	cout << i1*f1 << "\t" << f1*d1 << "\t" << (10%3==s1) << endl;
	cout << (s1==i2)*2 << "\t" << (i1==1 && ++i2==2) << "\t" << i2 << endl;
	cout << ((((f1*i2==d1*s1)*50)%9)==5*(1<=2))*123.456 << endl;
return 0;
}