from modele import*
from vue import*

#INITIALISATION
f = "game_files/maps/map_test.txt"
# f = open("game_files/maps/map_test.txt", "r", encoding="utf-8")
donjon, position, dragons = charge_fichier(f)
aventurier = Aventurier(position, 1)
chemin = []

elements = []
for i in range(len(donjon)):
    elements.append([])
    for j in range(len(donjon[i])):
        elements[i].append([])
for dragon in dragons:
    (x,y) = dragon.position
    elements[x][y] = dragon

dessine_niveau(donjon, dragons, aventurier)

while dragons != []:
    ev = donne_ev()
    tev = type_ev(ev)

    if tev == "Quitte":
        break

    elif tev == "ClicGauche":
        # Pivote la case sur laquelle on clique
        j, i = donne_position(donjon, abscisse(ev), ordonnee(ev))
        pivoter(donjon, (i, j))
        efface("chemin")
        dessine_portes(donjon, (i, j))

    elif tev == "ClicDroit":
        # Cherche le chemin vers le dragon le plus haut niveau
        chemin = intention(donjon, aventurier.position, dragons, elements)
        dessine_chemin(donjon, chemin)

    elif tev == "Touche":
        nom_touche = touche(ev)
        
        if nom_touche == "space":
            # L'aventurier affronte le dragon
            if chemin != []:
                if not combat(dragons, elements, aventurier, chemin):
                    print("PERDU")
                    break
                dessine_niveau(donjon, dragons, aventurier)
                chemin = []
                efface("chemin")
    mise_a_jour()
ferme_fenetre()
