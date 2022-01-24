import java.util.*;

public class Animal {
	public Animal(String nom, int nmb) {
		String id = nom;
		int age = nmb;
	}

	public static String stringInput() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Entrez le nom : ");
		String input = scanner.nextLine();
		scanner.close();
		return input;
	}

	public static int intInput() {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Entrez l'age : ");
		int input = 0;
		if(scanner.hasNextInt()) {
			input = scanner.nextInt();
		}
		scanner.close();
		return input;
	}

	public static Animal saisieAnimal() {
		String nom = stringInput();
		int age = intInput();
		Animal item = new Animal(nom, age);
		return item;
	}

	public static void main(String[] args) {
		Animal[] animaux = new Animal[2];
		for (int i = 0; i < animaux.length; i++) {
			animaux[i] = saisieAnimal();
		}
		System.out.println(animaux[0]);
	}
}