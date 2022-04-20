import pandas as pd

df = pd.read_csv('files/oligo.csv', sep=';')

def affichage():
	print(df, '\n') 						# DF entière
	print(list(df.columns), '\n')			# Nom des colonnes
	print(list(df.index), '\n')				# Nom des lignes
	print(df["Disease"], '\n')				# Colonnes 'Maladies'
	print(df.head(3), '\n')					# 3 premières lignes
	print(df.iloc[1])						# 2ème ligne

def find_entry(entry):
	for index in df.index:
		row = list(df.iloc[index])
		if entry in row:
			return list(row)[1]
	raise(KeyError("Le gène '{}' n'existe pas".format(entry)))

def quest():
	print("Gènes :",list(df["Oligo"]))
	query = input("Entrez un nom de gène : ")
	entry = find_entry(query)
	print(entry)

if __name__ == '__main__':
	# affichage()
	quest()
