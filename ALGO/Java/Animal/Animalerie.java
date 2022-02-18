
import java.util.*;
import java.nio.file.*;
// import java.lang.*;
import java.io.*;

// TODO :
// + - supprAnimal : redondance query base de données affichage liste + recherche par id

public class Animalerie extends ArrayList {
	static String id;

    public void ClearConsole() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

	private String stringInput(String prompt) {
		String input;
		Scanner scanner = new Scanner(System.in);
		while (true) {
			try {
				System.out.print(prompt);
				input = scanner.nextLine();
				if (input.equals("")) {throw new Exception("Entrée vide\n");}
				break;
			} catch (Exception e) {
				System.out.println("Erreur : Entrez un string");
				scanner.nextLine();
			}
		}
		// scanner.close();
		return input;
	}

	private int intInput(String prompt) {
		Scanner scanner = new Scanner(System.in);
		int input;
		while (true) {
			try {
				System.out.print(prompt);
				input = scanner.nextInt();
				break;
			} catch (Exception e) {
				System.out.println("Erreur : Entrez un entier");
				scanner.nextLine();
			}
		}
		return input;
	}

	public void export_animalerie() {
		char sep = ',';
		String fileName = stringInput("Entrez le nom du fichier [.csv] : ");
		fileName = fileName+".csv";
		try {
			FileWriter writer = new FileWriter(fileName);
			for (int i = 0; i < size(); i++) {
				Animal item = (Animal)get(i);
	  			writer.write(item.id + sep + item.age + sep + item.type() + System.lineSeparator());
			}
			writer.close();
		} catch (Exception e) {
			System.out.println("An error occurred while writing to file " + fileName);
		}
		System.out.println("Sauvegarde effectuée avec succès.");
	}

	public void saisieAnimal() {
		ClearConsole();
		System.out.println("-- Ajouter un animal --");
		System.out.println("Types supportés : Rat, Souris");
		String typeAnimal = stringInput("Quel type d'animal : ");
		typeAnimal = typeAnimal.toLowerCase();
		int n = intInput("Combien d'animaux à ajouter : ");
		switch (typeAnimal) {
			case "rat":
				for (int i = 0; i < n; i++) {
					String nom = stringInput("Entrez le nom : ");
					int age = intInput("Entrez l'age : ");
					Animal item = new Rat(nom, age);
					add(item);
				}
				break;
			case "souris":
				for (int i = 0; i < n; i++) {
					String nom = stringInput("Entrez le nom : ");
					int age = intInput("Entrez l'age : ");
					Animal item = new Souris(nom, age);
					add(item);
				}
				break;
		}
	}

	public int getIndex(String query) {
		String name;
		for (int i = 0; i < size(); i++) {
			Animal item = (Animal)get(i);
			name = item.id;
			if (name.equals(query)) {
				return i;
			}
		}
		return -1;
	}


	public void supprAnimal() {
		int query_index;
		System.out.println("-- Supprimer un animal --");
		System.out.println("Animaux trouvés dans la base de données ("+size()+") :");
		for (int i = 0; i < size(); i++) {
			Animal item =  (Animal)get(i);
			System.out.print(item.id+", ");
		}
		System.out.println();
		String query = stringInput("Entrez le nom de l'animal : ");
		query_index = getIndex(query);
		if (query_index == -1) 	{System.out.println("Animal introuvable.");} 
		else 					{remove(query_index);}
	}

	public void print_menu() {
		System.out.println("1. Créer des entrées");
		System.out.println("2. Supprimer des entrées");
		System.out.println("3. Afficher les entrées");
		System.out.println("4. Exporter l'animalerie");
		System.out.println("0. Quitter");
		System.out.println();
	}

	public void afficher() {
		System.out.println("-- Animaux trouvés --");
		for (int i = 0; i < size() ; i++) {
			Animal item = (Animal)get(i);
			item.info();
		}
	}

	public void menu() {
		print_menu();
		int choix = intInput("Choix : ");
		switch(choix) {
			case 0:
				System.exit(0);
			case 1: // Créer
				ClearConsole();
				saisieAnimal();
				break;
			case 2: // Supprimer
				ClearConsole();
				supprAnimal();
				break;
			case 3: // Afficher
				ClearConsole();
				afficher();
				break;
			case 4:
				ClearConsole();
				export_animalerie();
				break;
		}
	}

	public void start() {
		ClearConsole();
		while (true) {
			System.out.println(size());
			menu();
		}
	}
}