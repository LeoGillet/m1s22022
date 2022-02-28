class Arbre:
	def __init__(self):
		self.racine = None
		self.nodes = []

	def taille(self):
		return taille_sous_arbre(self.racine)

	def hauteur(self):
		return hauteur_sous_arbre(self.racine)

	def parcours_prefixe(self):
		return parc_prefixe(self.racine)

	def parcours_postfixe(self):
		return parc_postfixe(self.racine)



class Sommet:
	def __init__(self, etiq: str, pere=None):
		self.pere = pere
		self.etiq = etiq
		self.fils = []
	def hauteur(self):
		if self.pere is None:
			return 0
		return self.pere.hauteur()+1

def creer_sommet(t, s):
	if type(s) is list:
		for sommet in s:
			creer_sommet(t, sommet)
	elif type(s) is Sommet:
		if s.pere is None and t.racine is None:
			t.racine = s
		elif s.pere is None:
			print('Un arbre ne peut avoir deux racines')
		else:
			s.pere.fils.append(s)
		t.nodes.append(s)
	else:
		return NotImplemented
	
def taille_sous_arbre(s: Sommet):
	res = 1
	for fils in s.fils:
		res += taille_sous_arbre(fils)
	return res

def hauteur_sous_arbre(s: Sommet):
	hauteur = 0	
	if len(s.fils) == 0:
		return 0
	for fils in s.fils:
		hauteur_fils = hauteur_sous_arbre(fils)
		if hauteur_fils > hauteur:
			hauteur = hauteur_fils
	return hauteur+1

def parc_prefixe(s: Sommet):
	print(s.etiq)
	for fils in s.fils:
		parc_prefixe(fils)

def parc_postfixe(s: Sommet):
	for fils in s.fils:
		parc_prefixe(fils)
	print(s.etiq)

def parc_largeur(s: Sommet):
	[print(s.etiq) if s.pere is None else ""]
	parc = []
	for fils in s.fils:
		parc.append(fils)
		print(fils.etiq)
		parc_largeur(fils)




