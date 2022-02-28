class HelloPlus {
	static public void main(String[] args) {
		if (args.length < 1) {
			System.out.println("Hello X !");	
		} else { 
			for (int i = 0; i < args.length; i++) {
				System.out.println("Hello " + args[i] + " !");
			}
		}
	}
}