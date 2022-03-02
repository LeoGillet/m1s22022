# sommet1 = {id = 0,
#           valeur = 13,
#           pere = sommet2,
#           fils = [1, 3, 5]
#           }


#   racine(A) = 9
#   pere(A) = {9: None, 5: 9, 1: 9, 3: 9, 7: 5, 10: 3, 11: 3}
#   fils(A) = {9: [5, 1, 3], 5: [7], 1: [], 3: [10, 11], 10: [], 11: []}
#   etiquette(A) = {9: 'e', 5: 'b', 1: 'b', 3: 'c', 7: 'f', 11: 'r', 10: 'g'}

# Non, un arbre = une seule racine
#

def fils(A, p):
    liste_fils = []
    for sommet in A:
        for fils in sommet['fils']:
            liste_fils.append(fils)

