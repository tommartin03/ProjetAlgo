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
   #Todo
   return None

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
    print(VerifGrapheEulerien(graphe))

if __name__ == "__main__":
    main()

