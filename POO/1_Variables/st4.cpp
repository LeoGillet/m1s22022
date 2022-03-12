#include <iostream>
using namespace std;
int x;
void reset_x() {
   x=0;
}


int SOMME(int x) {
   return x+x;
}

int main(void){
   // effet de bord 1
   int val=3;
   cout << SOMME(val++) << endl; //équivaut à cout << (val+++val++) << endl;
   cout << SOMME(val++) << endl;
   cout << val << endl;
      
   // effet de bord 2
   int x=12; // variable déclarée en externe à main
   cout << x << endl;
   reset_x();
   cout << x << endl;
   return 0;
}