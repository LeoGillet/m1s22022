public class Animal {
	String id;
	int age;

	Animal(String nom, int age) {
		this.id = nom;
		this.age = age;
	}

	public void info() {
		System.out.println("----------------");
		System.out.println("Animal : "+id);
		System.out.println("Age : "+age);
		System.out.println("----------------");
		System.out.println("\n");
	}
}