#include <iostream>
#include <string>
using namespace std;

string ask(string prompt) {
	string choice;
	cout << prompt;
	cin >> choice;
	return choice;
}

int main() {
	string choix_tva; double tva; double prix_ht; double prix_ttc;

	double n_pates = stod(ask("Combien de kilos de pâtes avez vous acheté? : "));
	double prix_pates = stod(ask("Combien coûte le kilo de pâtes : "));
	double n_pq = stod(ask("Combien de rouleaux de PQ avez vous acheté? : "));
	double prix_pq = stod(ask("Combien coûte le rouleau de PQ ? : "));

	while (true) {
		choix_tva = ask("Quelle est la TVA de ces deux produits (A: 5.5\%) (B: 19.6\%) ? : ");
		if (choix_tva != "A" || choix_tva != "B") {break;}
 	}
	if (choix_tva == "A") {
		tva = 0.055;
	} 
	if (choix_tva == "B") {
		tva = 0.196;
	}

	prix_ht = n_pates*prix_pates + n_pq*prix_pq;
	prix_ttc = prix_ht + tva*prix_ht;

	cout << "Le prix HT est de " << prix_ht << "€ et le prix TTC est de " << prix_ttc << "€." << endl;
	return 0;
}