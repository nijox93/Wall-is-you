from modele import*
from vue import*

#INITIALISATION
f = "game_files/maps/map_test.txt"
# f = open("game_files/maps/map_test.txt", "r", encoding="utf-8")
donjon, position, dragons = charge_fichier(f)
pos_dragons = position_dragons(dragons)
aventurier = Aventurier(position, 1)
chemin = intention(donjon, position, pos_dragons)

dessine_donjon(donjon, dragons, aventurier)
dessine_aventurier(donjon, aventurier.position)
dessine_chemin(donjon, chemin)
for pos in pos_dragons:
    dessine_dragon(donjon, pos)

while(True):
    ev = donne_ev()
    tev = type_ev(ev)
    if tev == "Quitte":
        break
    elif tev == "ClicGauche":
        for i in range(len(donjon)):
            for j in range(len(donjon)):
                pivoter(donjon, (i, j))
                dessine_portes(donjon, (i, j))
    elif tev == "ClicDroit":
        chemin = intention(donjon, position, pos_dragons)
        print(chemin)
        dessine_chemin(donjon, chemin)
    mise_a_jour()
ferme_fenetre()
