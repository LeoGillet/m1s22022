#include <iostream>
#include <string>
#include <fstream>

using namespace std; // utilisation de l'espace de nom de std
void write_data(string filename, string content){
	ofstream file(filename);
	if (file) {
		file << content;
		file.close();
	} else {cout << "Erreur" << endl;}
}


int main(){
	string filename="data_01.txt";
	string content="nom\tprenom\nAA\taa\nBB\tbb\nCC\tcc\n";
	write_data(filename,content);
	return 0;
}