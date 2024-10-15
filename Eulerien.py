import json
from random import choice
from copy import deepcopy


def est_connexe(G, S0=None, atteint=None, profondeur=0):
    """
    Fonction qui indique si le graphe G est connexe.
    """
    if not atteint: 
        atteint = []
        
    # Si on a atteint tous les sommets, le graphe est connexe.
    if len(atteint) == len(G): 
        return True
    
    # Si on a effectué suffisamment de profondeur et qu'on n'a pas atteint tous les sommets, il n'est pas connexe.
    if profondeur >= len(G): 
        return False
    
    # On choisit un sommet de départ.
    if not S0: 
        S0 = choice([S for S in G])
        atteint.append(S0)
        profondeur += 1
    
    # Pour chaque sommet déjà atteint, on complète la liste avec les sommets que l'on peut atteindre.
    for S in atteint:
        for adj in G[S]:
            if adj not in atteint:
                atteint.append(adj)
    
    return est_connexe(G, S0, atteint, profondeur + 1)      

def VerifGrapheEulerien(G):
    """
    Vérifie si un graphe est eulérien.
    Un graphe est eulérien s'il est connexe et que tous ses sommets ont un degré pair.
    """
    G = deepcopy(G)

    # Vérification de la connexité.
    if not est_connexe(G):
        print("Le graphe n'est pas connexe, donc il n'y a ni chaîne ni cycle eulérien.")
        return False

    # Vérification des degrés pairs.
    for sommet in G:
        if len(G[sommet]) % 2 != 0:
            print(f"Le sommet {sommet} a un degré impair, donc le graphe n'est pas eulérien.")
            return False

    return True

def TestCycleEulerien(G, C):
    """
    Vérifie si la liste C est un cycle eulérien de G
    """
    est_passe = [] #liste ou l'on met toutes les arêtes ou l'on est passé
    for i in range (len(C)-1): 
        #on vérifie que C[i+1] est bien voisin de C[i] dans le graphe
        if C[i+1] in G[C[i]]:
            #on verifie qu'on a pas déjà pris cette arêtes 
            if [C[i],C[i+1]] not in est_passe and [C[i+1],C[i]] not in est_passe:
                est_passe.append([C[i],C[i+1]])
            else:
                print([C[i],C[i+1]])
                return False
        else:
            print(C[i+1],",", G[C[i]])
            return False
    #on verifie qu'on est bien passé par toute les arêtes 
    if(len(est_passe) == nombre_aretes(G)):
        return True
    else:
        
        return False
     
def nombre_aretes(graphe):
    """
    Calcule le nombre d'arêtes dans un graphe.
    
    :param graphe: Dictionnaire représentant le graphe sous forme d'adjacence.
    :return: Nombre d'arêtes.
    """
    count = 0
    for sommet, adjacents in graphe.items():
        count += len(adjacents)
    
    # Comme le graphe est non orienté, chaque arête est comptée deux fois.
    return count // 2

def EstIsthme(G, e):
    """
    Vérifie  si l’arête e est un isthme de G
    """

    #Todo
    return None

def Fleury(G,u):
    #Todo
   return None

def lire_graphe_json(fichier):
    with open(fichier, 'r') as f:
        graphe = json.load(f)
    graphe = {int(k): v for k, v in graphe.items()}
    return graphe

def main():
    graphe = lire_graphe_json("graphes.json")
    C = [1, 2, 4, 3, 2, 5, 1,6,7,1]
    print(TestCycleEulerien(graphe,C))
    print(VerifGrapheEulerien(graphe))

if __name__ == "__main__":
    main()

