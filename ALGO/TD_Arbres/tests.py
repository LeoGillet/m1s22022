from impl2 import *

tree = Arbre()
a = Sommet('a', pere=None)
b = Sommet('b', pere=a)
c = Sommet('c', pere=a)
d = Sommet('d', pere=a)
e = Sommet('e', pere=c)
f = Sommet('f', pere=d)
g = Sommet('g', pere=d)
h = Sommet('h', pere=f)

sommets = [a, b, c, d, e, f, g, h]
creer_sommet(tree, sommets)

parc_largeur(tree.racine)
