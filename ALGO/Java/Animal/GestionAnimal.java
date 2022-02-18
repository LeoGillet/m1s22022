
import java.util.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.lang.*;
import java.io.*;

// TODO : 
// + - supprAnimal : redondance query base de données affichage liste + recherche par id

public class GestionAnimal {
	public static void ClearConsole() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

	public static List<Animalerie> animaleries = new ArrayList<Animalerie>();
	public static List<String> names = new ArrayList<String>();

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


	public static Animalerie import_file() {
		String animal_type; Rat rat; Souris souris; char SEPARATOR = ',';
		String filename = stringInput("Entrez le nom du fichier à importer : ");
		String short_filename = filename.substring(0, filename.length()-4);
		Animalerie animaux = new Animalerie(); names.add(short_filename);
		List<String> lines = Collections.emptyList();
		try {
			lines = Files.readAllLines(Paths.get(filename), StandardCharsets.UTF_8);
		} catch (IOException e) {
			e.printStackTrace();
		}
		String sep = new Character(SEPARATOR).toString();
		for (String line : lines) {
			// 0: name, 1: age, 2: type
			String[] animal_info = line.split(sep);
			switch (animal_info[2]) {
				case "rat":
					rat = new Rat(animal_info[0], Integer.parseInt(animal_info[1]));
					animaux.add(rat);
					break;
				case "souris":
					souris = new Souris(animal_info[0], Integer.parseInt(animal_info[1]));
					animaux.add(souris);
					break;
			}
		}
		return animaux;
	}



	public static void afficher_animaleries() {
		int i = 1; System.out.println();
		for (Animalerie animalerie : animaleries) {
			System.out.println(i + ". " + animalerie.id
				+ "(" + animalerie.size() + ")"); i++;
		}
	}

	public static void print_menu() {
		System.out.println("1. Créer une animalerie");
		System.out.println("2. Importer une animalerie");
		System.out.println("3. Modifier une animalerie");
		System.out.println("0. Quitter");
	}

	public static void creer_animalerie() {
		String name = stringInput("Entrez un nom d'animalerie [0: default] : ");
		if (name == "0") {name = "default";}
		Animalerie animaux = new Animalerie();
		names.add(name);
		animaleries.add(animaux);
	}

	public static void edit_animalerie() {
		System.out.println();
		for (int i = 0; i < animaleries.size(); i++) {
			System.out.println();
		}
	}

	public static void menu() {
		print_menu();
		int choix = intInput("Choix : ");
		switch(choix) {
			case 0:
				System.exit(0);
			case 1:
				creer_animalerie();
				break;
			case 2: // Créer
				animaleries.add(import_file());
				break;
			case 3: // Supprimer
				ClearConsole();
				afficher_animaleries();
				choix = intInput("Choix : ");
				animaleries.get(choix-1).start();
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