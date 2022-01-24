import java.util.*;
// import java.lang.*;
// import java.io.*;

// TODO : 
// +++ - lever exceptions quand saisie empêche conversion str>int
// + - supprAnimal : redondance query base de données affichage liste + recherche par id

public class Animaux {
	public static void ClearConsole(){
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

	static class Animal {
		String id;
		int age;
	}

	public static Animal[] arr_animaux = new Animal[100];
	public static int n_animaux = 0;

	private static String stringInput(String prompt) {
		Scanner scanner = new Scanner(System.in);
		System.out.print(prompt);
		String input = scanner.nextLine();
		// scanner.close();
		return input;
	}

	private static int intInput(String prompt) {
		Scanner scanner = new Scanner(System.in);
		System.out.print(prompt);
		int input = scanner.nextInt();
		// scanner.close();
		return input;
	}

	public static void saisieAnimal() {
		ClearConsole();
		int n = intInput("Combien d'animaux à ajouter : ");
		for (int i = 0; i < n; i++) {
			String nom = stringInput("Entrez le nom : ");
			int age = intInput("Entrez l'age : ");
			Animal item = new Animal();
			item.id = nom;
			item.age = age;
			arr_animaux[n_animaux] = item;
			n_animaux++;
		}
	}
	public static void affichage() {
		for (int i = 0; i < n_animaux; i++) {
			System.out.println("----------------");
			System.out.println("Animal : "+arr_animaux[i].id);
			System.out.println("Age : "+arr_animaux[i].age);
			System.out.println("----------------");
			System.out.println("\n");
		}
	}

	public static int getIndex(String query) {
		int i = 0;
		while (i < n_animaux) {
			String name = arr_animaux[i].id;
			if (name.equals(query)) {
				return i;
			} else {
				i++;
			}
		}
		return -1;
	}


	public static void supprAnimal() {
		System.out.println("Animaux dans la base :");
		for (int i = 0; i < n_animaux; i++) {
			System.out.print(arr_animaux[i].id+" ("+arr_animaux[i].age+"), ");
		}
		String nom = stringInput("Nom de l'animal à retirer : ");
		int index = getIndex(nom);
		if (index > 0) {
			Animal[] copy = new Animal[100];
			for (int i=0, j=0; i<100; i++) {
				copy[j++] = arr_animaux[i];
			}
			arr_animaux = copy;
			n_animaux -= 1;
		} else {
			System.out.println("Entrée introuvable");
		}
	}

	public static void print_menu() {
		System.out.println("1. Créer des entrées");
		System.out.println("2. Supprimer des entrées");
		System.out.println("3. Afficher les entrées");
		System.out.println();
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
				affichage();
		}
	}

	public static void main(String[] args) {
		while (true) {
			menu();
		}
	}
}