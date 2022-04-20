#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

vector<string> split(string value, string sep){
	vector<string> words;
	int pos = 0; string word;
	while ((pos = value.find(sep)) != string::npos) {
	    word = value.substr(0, pos);
	    value.erase(0, pos + sep.length());
		words.push_back(word);
	}
	return words;
}

string read_data(string filename) {
	ifstream fichier(filename);
	string text; string line;

	if (fichier) {
		while(getline(fichier, line)) {
			text += line+"\n";
		}
		fichier.close();
	} else {cout << "Erreur" << endl;}
	return text;
}

double str_to_double(string value){
	return stod(value);
}

vector<double> vstr_to_double(vector<string> values){
	vector<double> convertedValues;
	for (const string& value : values) {
		convertedValues.push_back(str_to_double(value));
	}
	return convertedValues;
}

double mean(vector<double> values){
	double sum;
	for (const double& value : values) {
		sum += value;
	}
	return sum/values.size();
}

int main(int argc, char** argv) {
	if (argc > 1) {
		string data = read_data(argv[1]);
		vector<double> notes=vstr_to_double(split(data,"\n"));
		cout << "moyenne : " << mean(notes) << endl;
	return 0;
	}
	return 0;
}

int main(){
	
}