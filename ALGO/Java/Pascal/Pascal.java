public class Pascal {
	private static final int DIM = 10;

	public static void init(int[][] tableau) {
		for (int i = 0; i < DIM; i++) {
			for (int j = 0; j < DIM; j++) {
				tableau[i][j] = 0;
			}
		}
	}

	public static void affiche(int[][] tableau) {
		for (int i = 0; i < DIM; i++) {
			System.out.println("");
			for (int j = 0; j < DIM; j++) {
				int val = tableau[i][j];
				if (val != 0) {
					System.out.print(val + " ");
				}
			}
		}
	}


	public static void main(String[] args) {
		int[][] tab = new int[DIM][DIM];
		init(tab);
		tab[0][0] = 1;
		for (int i = 1; i < DIM; i++) {
			tab[i][0] = 1;
			for (int j = 1; j <= i; j++) {
				tab[i][j] = tab[i-1][j-1] + tab[i-1][j];
			}
		}
		affiche(tab);
	}
}