def creer_arbre(racine=None):
    return {
        'racine' : racine
    }

def creer_sommet(h, l, ori, posNO, posSE, billes=[]):
    return {
        'pere' : None,
        'etiquette' : {'hauteur': h, 'largeur': l, 'orientation': ori,
                       'billes': billes, 'NO': posNO, 'SE': posSE},
        'fils_gauche' : 0,
        'fils_droite' : 0,

    }

def inserer_fils_gauche(pere,fils):
    fils["pere"] = pere
    pere["fils_gauche"] = fils
    return fils

def inserer_fils_droite(pere,fils):
    fils["pere"] = pere
    pere["fils_droite"] = fils

def inserer_racine(arbre,racine):
    arbre["racine"] = racine

def racine(A):
    return A["racine"]

def fils_gauche(s):
    return s["fils_gauche"]

def fils_droit(s):
    return s["fils_droite"]

def pere(s):
    return s["pere"]

def etiquette(s):
    return s["etiquette"]

# def taille_arbre(A):
#     taille_sous_arbre(A["racine"])

# def taille_sous_arbre(s):
#     if fils_gauche(s) is None and fils_droit(s) is None :
#         return 0
#     else :
#         return 1 + taille_sous_arbre(s["fils_gauche"]) + taille_sous_arbre(s["fils_droite"])


arb = creer_arbre()
root = creer_sommet("a")
inserer_racine(arb, root)
s1 = creer_sommet("b")
s2 = creer_sommet("c")
s3 = creer_sommet("d")
s4 = creer_sommet("c")
s5 = creer_sommet("e")
inserer_fils_droite(root,s1)
inserer_fils_gauche(root,s2)
inserer_fils_gauche(s1,s3)
inserer_fils_droite(s3,s4)
inserer_fils_gauche(s2,s5)
# print(taille_arbre(arb))