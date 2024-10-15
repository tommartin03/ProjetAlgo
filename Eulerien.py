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

def TestCycleEulerien(G, cycle):
   #Todo
   return None

# Exemple de graphe G1
G2_correct = {
    '1': ['5', '3'],
    '2': ['A', 'D', 'C'],
    '3': ['A', 'B', 'D'],
    '4': ['B', 'C', 'E'],
    '5': ['D']
}


print(VerifGrapheEulerien(G2_correct))
cycle_test = ['A', 'C', 'D', 'A', 'E', 'B', 'D', 'E', 'A']
is_cycle_eulerian = TestCycleEulerien(G2_correct, cycle_test)
print("Le cycle est eulérien :", is_cycle_eulerian)
