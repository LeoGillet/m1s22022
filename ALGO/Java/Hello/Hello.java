class Hello {
	static public void main(String[] args) {
		if (args.length < 1) {
			System.out.println("Hello X !");	
		} else {
			System.out.println("Hello " + args[0] + " !");
		}
	}
}