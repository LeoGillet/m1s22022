// code_15_1.cpp
#include <iostream>
#include <vector>
using namespace std;

void fa1(int value){
	value=value+20;
}
void fa2(int& value){
	value=value+20;
}

void fv1(vector<int> value){
	value.at(0)=value.at(0)+20;
}

void fv2(vector<int>& value){
	value.at(0)=value.at(0)+20;
}

int main(){
	int a=10;
	vector<int> v{1,2,3};
	cout << "a : " << a << "\t et v.at(0) : " << v.at(0) << endl;
	fa1(a);fv1(v);
	cout << "a : " << a << "\t et v.at(0) : " << v.at(0) << endl;
	fa2(a);fv2(v);
	cout << "a : " << a << "\t et v.at(0) : " << v.at(0) << endl;
	return 0;
}