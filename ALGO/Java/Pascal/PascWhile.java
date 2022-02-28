public class PascWhile {
	private static final int DIM = 10;

	public static void init(int[][] tableau) {
		int i = 0;
		int j = 0;
		while (i < DIM) {
			while (j < DIM) {
				tableau[i][j] = 0;
				j++;
			}
			i++;
		}
	}

	public static void affiche(int[][] tableau) {
		int i = 0;
		int j = 0;
		while (i < DIM) {
			System.out.println("");
			while (j < DIM) {
				int val = tableau[i][j];
				if (val != 0) {
					System.out.print(val + " ");
				}
				j++;
			}
			i++;
		}
	}


	public static void main(String[] args) {
		int[][] tab = new int[DIM][DIM];
		init(tab);
		tab[0][0] = 1;
		int i = 1;
		int j = 1;
		while (i < DIM) {
			tab[i][0] = 1;
			while (j <= i) {
				tab[i][j] = tab[i-1][j-1] + tab[i-1][j];
				j++;
			}
			i++;
		}
		affiche(tab);
	}
}