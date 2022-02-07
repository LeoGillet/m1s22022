
import java.util.*;
// import java.lang.*;
// import java.io.*;

// TODO : 
// + - supprAnimal : redondance query base de données affichage liste + recherche par id

public class Animalerie {
	public static void ClearConsole(){
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

	public static List<Animal> arr_animaux = new ArrayList<Animal>();

	private static String stringInput(String prompt) {
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

	private static int intInput(String prompt) {
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

	public static void saisieAnimal() {
		ClearConsole();
		int n = intInput("Combien d'animaux à ajouter : ");
		for (int i = 0; i < n; i++) {
			String nom = stringInput("Entrez le nom : ");
			int age = intInput("Entrez l'age : ");
			Animal item = new Animal(nom, age);
			arr_animaux.add(item);
		}
	}
	

	public static int getIndex(String query) {
		String name;
		for (int i = 0; i < arr_animaux.size(); i++) {
			name = arr_animaux.get(i).id;
			if (name.equals(query)) {
				return i;
			}
		}
		return -1;
	}


	public static void supprAnimal() {
		int query_index;
		System.out.println("-- Supprimer un animal --");
		System.out.println("Animaux trouvés dans la base de données ("+arr_animaux.size()+") :");
		for (int i = 0; i < arr_animaux.size(); i++) {
			System.out.print(arr_animaux.get(i).id+", ");
		}
		System.out.println();
		String query = stringInput("Entrez le nom de l'animal : ");
		query_index = getIndex(query);
		if (query_index == -1) 	{System.out.println("Animal introuvable.");} 
		else 					{arr_animaux.remove(query_index);}
	}

	public static void print_menu() {
		System.out.println("1. Créer des entrées");
		System.out.println("2. Supprimer des entrées");
		System.out.println("3. Afficher les entrées (WIP)");
		System.out.println();
	}

	public static void afficher() {
		for (int i = 0; i < arr_animaux.size() ; i++) {
			arr_animaux.get(i).info();
		}
	}

	public static void menu() {
		print_menu();
		int choix = intInput("Choix : ");
		switch(choix) {
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
		}
	}

	public static void main(String[] args) {
		ClearConsole();
		while (true) {
			menu();
		}
	}
}