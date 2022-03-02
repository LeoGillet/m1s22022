from trees import *

def coupe(sommet, sens):
    hauteur = sommet['hauteur']
    largeur = sommet['largeur']
    x = sommet['NO'][0]
    y = sommet['NO'][1]
    if sens == 'verticale':
        posNO_1 = sommet['NO'] # salle gauche
        posSE_1 = x+largeur/2, y+hauteur
        posNO_2 = x+largeur/2, y # salle droite
        posSE_2 = sommet['SE']
    else: # horizontale
        posNO_1 = sommet['NO'] # salle haut
        posSE_1 = x+largeur, y+hauteur/2
        posNO_2 = x, y+hauteur/2 # salle bas
        posSE_2 = sommet['SE']
    inserer_fils_gauche(hauteur, largeur/2, 'verticale',
                        posNO_1, posSE_1)
    inserer_fils_droite(hauteur, largeur/2, 'verticale',
                        posNO_2, posSE_2)


def construire_arbre_collision(H, L, nb_etape):
    return False