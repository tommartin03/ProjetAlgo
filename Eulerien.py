import json
from random import choice
from copy import deepcopy


def est_connexe(G, S0=None, atteint=None, profondeur=0):
    """
    Fonction qui indique si le graphe G est connexe.
    """
    if not atteint: 
        atteint = []   
    if len(atteint) == len(G): 
        return True
    if profondeur >= len(G): 
        return False
    if not S0: 
        S0 = choice([S for S in G])
        atteint.append(S0)
        profondeur += 1
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
    if not est_connexe(G):
        print("Le graphe n'est pas connexe, donc il n'y a ni chaîne ni cycle eulérien.")
        return False
    for sommet in G:
        if len(G[sommet]) % 2 != 0:
            print(f"Le sommet {sommet} a un degré impair, donc le graphe n'est pas eulérien.")
            return False
    return True

def TestCycleEulerien(G, C):
    """
    Vérifie si la liste C est un cycle eulérien de G
    """
    est_passe = [] 
    for i in range (len(C)-1): 
        if C[i+1] in G[C[i]]:
            if [C[i],C[i+1]] not in est_passe and [C[i+1],C[i]] not in est_passe:
                est_passe.append([C[i],C[i+1]])
            else:
                print([C[i],C[i+1]])
                return False
        else:
            print(C[i+1],",", G[C[i]])
            return False
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
    return count // 2


def EstIsthme(G, e):
    """
    Vérifie si l’arête e = (u, v) est un isthme de G.
    Une arête e est un isthme si sa suppression déconnecte les sommets qu'elle relie.
    """
    G = deepcopy(G)
    u, v = e
    G[u].remove(v)
    G[v].remove(u)
    if not est_connexe(G):
        return True
    return False


def Fleury(G, S):
    """
    Algorithme de Fleury pour trouver un cycle eulérien dans un graphe.
    """
    G = deepcopy(G)
    cycle = [S]
    while len(G[S]) > 0:
        for i, S_suivant in enumerate(G[S]):
            if not EstIsthme(G, [S, S_suivant]):
                break
        cycle.append(S_suivant)
        G[S].remove(S_suivant)
        G[S_suivant].remove(S)
        S = S_suivant
    return cycle

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
    print(EstIsthme(graphe,[2,3]))
    print(Fleury(graphe,1))

if __name__ == "__main__":
    main()

