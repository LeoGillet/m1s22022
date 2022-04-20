#include <iostream>
#include <string>
using namespace std; // utilisation de l'espace de nom de std


bool check_mail(string mail) {
	if (mail.find('@') != string::npos) return true;
	return false;
}


int main() {
	string mail1="aaa.bbb@ccc.ddd";
	string mail2="aaa.bbb_ccc.ddd";
	string mail3="aaa@ccc.ddd";
	string mail4="aaa.bbb@ccc";
	if (check_mail(mail1)) cout << mail1 << " contient @" << endl;
	if (check_mail(mail2)) cout << mail2 << " contient @" << endl;
	if (check_mail(mail3)) cout << mail3 << " contient @" << endl;
	if (check_mail(mail4)) cout << mail4 << " contient @" << endl;
	return 0;
}