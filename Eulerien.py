from random import choice
from copy import deepcopy

def est_complet(G):
    """
    Fonction qui indique si le graphe G est complet.
    """
    for S0 in G:
        for S in G:
            # S'il existe deux sommets non reliés, le graphe n'est pas complet.
            if S != S0 and S not in G[S0]:
                return False
    return True

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

def non_oriente(G):
    """
    Vérifie si le graphe G est non orienté.
    """
    for S0 in G:
        for S in G[S0]: 
            # S'il existe une arête non réciproque, le graphe est orienté.
            if S0 not in G[S]: 
                return False
    return True

def VerifGrapheEulerien(G):
    """
    Vérifie si un graphe est eulérien.
    Un graphe est eulérien s'il est connexe et que tous ses sommets ont un degré pair.
    """
    G = deepcopy(G)

    # Vérification si le graphe est non orienté.
    if not non_oriente(G):
        print("Arrêt. Le graphe soumis est un graphe orienté.")
        return False

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
    """
    Vérifie si une liste de sommets représente un cycle eulérien.
    Le cycle doit passer par chaque arête exactement une fois et revenir au point de départ.
    """
    G = deepcopy(G)
    
    # Vérifier que le cycle commence et se termine au même sommet
    if cycle[0] != cycle[-1]:
        return False
    
    # Parcourir chaque sommet du cycle
    for i in range(len(cycle) - 1):
        u, v = cycle[i], cycle[i + 1]
        
        # Vérifier si l'arête (u, v) existe
        if v not in G[u]:
            return False
        
        # Supprimer l'arête (u, v) du graphe
        G[u].remove(v)
        G[v].remove(u)

    # Vérifier que toutes les arêtes ont été utilisées
    for voisins in G.values():
        if voisins:
            return False

    return True

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
