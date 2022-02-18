def creer_arbre_vide():
    return {
    'racine' : None,
    'etiquettes' : {},
    'fils_droit' : {},
    'fils_gauche' : {},
    'pere' : {}
    }
def inserer_ab(A, pere, fils, etiquette=None, type_fils=None):
    if fils is None:
        return
    if not pere is None:
        A[type_fils][pere] = fils
        A['pere'][fils] = pere
        A['fils_gauche'][fils] = None
        A['fils_droit'][fils] = None
        A['etiquettes'][fils] = etiquette

def inserer_fils_gauche(A, pere, fils, etiquette=None):
    inserer_ab(A, pere, fils, etiquette=etiquette, type_fils='fils_gauche')

def inserer_fils_droit(A, pere, fils, etiquette=None):
    inserer_ab(A, pere, fils, etiquette=etiquette, type_fils='fils_droit')

def inserer_racine(A, racine, etiquette=None):
    A['racine'] = racine
    inserer_ab(A, None, racine, etiquette, type_fils=None)

def creer_arbre(racine=None, etiquette=None):
    res = creer_arbre_vide()
    inserer_racine(res, racine, etiquette)
    return res

def racine(A):
    return A['racine']

def fils_gauche(A, s):
    return A['fils_gauche'][s]

def fils_droit(A, s):
    return A['fils_droit'][s]

def pere(A, s):
    return A['pere'][s]

def etiquette(A, s):
    return A['etiquettes'][s]



#def hauteur_arbre(A):

arb = creer_arbre(4,"a")
rac = arb["racine"]
inserer_fils_droit(arb, 4, 5)
inserer_fils_gauche(arb, 4, 2)
inserer_fils_gauche(arb, 5, 1)



