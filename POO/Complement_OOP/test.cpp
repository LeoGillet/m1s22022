#include <iostream>
#include <cmath>
using namespace std;

void square(double val) {
  cout << "Type: " << typeid(val).name() << " : " << pow(val, 2) << endl;
}

void square(char val) {
  cout << "Type: " << typeid(val).name() << " : " << pow(val, 2) << endl;
}

void square(float val) {
  cout << "Type: " << typeid(val).name() << " : " << pow(val, 2) << endl;
}

void square(int val) {
  cout << "Type: " << typeid(val).name() << " : " << pow(val, 2) << endl;
}

int main() {
  char a=2;
  int b=3;
  float c=4.4;
  double d=5.5;
  square(a);
  square(b);
  square(c);
  square(d);
  return 0;
}
