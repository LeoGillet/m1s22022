String mot = "abc";

mot.equals("abc"); // true
mot == "abc"; // error

int nombre = 4;
String nombre_to_mot = String.valueOf(nombre); // '4' String

int mot_to_nombre = Integer.parseInt(nombre_to_mot); // 4 int
double mot_to_double = Double.parseDouble(nombre_to_mot);

void print()
	{
		System.out.println('nombre'+nombre);
		System.out.println('mot'+mot);
	}