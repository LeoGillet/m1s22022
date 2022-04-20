#include <iostream>
#include <string>
#include <vector>
using namespace std; // utilisation de l'espace de nom de std

bool check_mail(string mail){
	if (mail.find('@') != string::npos) return true;
	return false;
}

void display(vector<string> value){
	for (const string& mail : value) {
		cout << mail << endl;
	}
}

vector<string> mail_tokens(string mail){
...
}

int main(){
	string mail1="aaa.bbb@ccc.ddd";
	string mail2="aaa.bbb_ccc.ddd";
	string mail3="aaa@ccc.ddd";
	string mail4="aaa.bbb@ccc";
	cout << mail1 << endl;
	display(mail_tokens(mail1));
	cout << mail2 << endl;
	display(mail_tokens(mail2));
	cout << mail3 << endl;
	display(mail_tokens(mail3));
	cout << mail4 << endl;
	display(mail_tokens(mail4));
	return 0;
}