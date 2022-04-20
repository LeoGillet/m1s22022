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

vector<string> get_mails(void){
	bool finished = false;
	vector<string> mails = {};
	string input;
	while (!finished) {
		cout << "entrez le mail : ";
		cin >> input;
		cout << endl;
		if (check_mail(input)) mails.push_back(input);
		else if (input == "stop") finished = true;
		else cout << "Il manque un @." << endl;
	} 
	return mails;
}

int main(void){
	vector<string> result=get_mails();
	display(result);
	return 0;
}