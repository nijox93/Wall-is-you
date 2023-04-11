#CLASSES
class Aventurier():
    def __init__(self, position, niveau):
        self.position = position
        self.niveau = niveau


class Dragon():
    def __init__(self, position, niveau):
        self.position = position
        self.niveau = niveau


#FONCTIONS
def connecte(donjon, p1, p2):
    ''' Vérifie si deux salles sont connectées ou pas '''
    portes1, portes2 = donjon[p1[0]][p1[1]], donjon[p2[0]][p2[1]]
    if p1[0] == p2[0]:
        return ((portes1[1] and portes2[3])
                or (portes1[3] and portes2[1]))
    elif p1[1] == p2[1]:
        return ((portes1[0] and portes2[2])
                or (portes1[2] and portes2[0]))
    return False


def pivoter(donjon, position):
    ''' Pivote une case '''
    t = donjon[position[0]][position[1]]
    t[0], t[1], t[2], t[3] = t[3], t[0], t[1], t[2]
    donjon[position[0]][position[1]] = t
    return donjon


def Voisines(donjon, position):
    ''' Renvoie les voisines disponibles '''
    voisines = []
    if position[0] > 0:
        p2 = (position[0] - 1, position[1])
        voisines.append(p2)
    if position[1] < len(donjon[0]) - 1:
        p2 = (position[0], position[1] + 1)
        voisines.append(p2)
    if position[0] < len(donjon) - 1:
        p2 = (position[0] + 1, position[1])
        voisines.append(p2)
    if position[1] > 0:
        p2 = (position[0], position[1] - 1)
        voisines.append(p2)
    return voisines


def intention(donjon, position, pos_dragons, visite=[]):
    ''' Renvoie une chemin possible de l'aventurier jusqu'au dragon '''
    visite.append(position)
    chemin = []
    if position in pos_dragons:
        return [position]
    voisines = Voisines(donjon, position)
    for voisine in voisines:
        if voisine not in visite:
            if connecte(donjon, position, voisine):
                chemin = intention(donjon, voisine, pos_dragons, visite)
                if chemin != []:
                    return [position] + chemin
    return chemin


def charge_grille(fichier):
    ''' Charge la grille du donjon '''
    grille = []
    salles = {'═': [False, True, False, True], '║': [True, False, True, False],
              '╔': [False, True, True, False], '╗': [False, False, True, True],
              '╚': [True, True, False, False], '╝': [True, False, False, True],
              '╠': [True, True, True, False], '╣': [True, False, True, True],
              '╦': [False, True, True, True], '╩': [True, True, False, True],
              '╨': [True, False, False, False], '╡': [False, False, False, True],
              '╥': [False, False, True, False], '╞': [False, True, False, False],
              '╬': [True, True, True, True]}
    i = 0
    for ligne in fichier:
        print("ligne: ", ligne)
        if ligne[0] == 'A':
            break
        grille.append([])
        for elem in ligne:
            grille[i].append(salles[elem])
        i += 1
    return grille


def charge_aventurier(fichier):
    ''' Charge la position de l'aventurier '''
    for ligne in fichier:
        if ligne[0] == 'A':
            ligne = ligne.split(" ")
            x, y = int(ligne[1]), int(ligne[2])
            break
    return (x, y)


def charge_dragons(fichier):
    ''' Charge la liste des dragons '''
    dragons = []
    for ligne in fichier:
        if ligne[0] == 'D':
            ligne = ligne.split(" ")
            x, y, niv = int(ligne[1]), int(ligne[2]), ligne[3]
            dragons.append(Dragon((x, y), niv))
    return dragons


def charge_fichier(fichier):
    ''' Charge les données d'une map '''
    #                                                 #
    ## AMELIORATION DE LA GESTION D'ERREURS POSSIBLE ##
    #                                                 #
    fichier = open(fichier, "r", encoding="utf-8")
    fichier = fichier.read().splitlines()
    donjon = charge_grille(fichier)
    position = charge_aventurier(fichier)
    dragons = charge_dragons(fichier)
    return donjon, position, dragons


def position_dragons(dragons):
    ''' Renvoie la liste des positions d'une liste de dragons '''
    positions = []
    for dragon in dragons:
        positions.append(dragon.position)
    return positions
