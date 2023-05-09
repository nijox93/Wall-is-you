from modele import*
from vue import*

#INITIALISATION
f = "game_files/maps/map_test.txt"
# f = open("game_files/maps/map_test.txt", "r", encoding="utf-8")
donjon, position, dragons = charge_fichier(f)
aventurier = Aventurier(position, 1)
chemin = []
# pos_dragons = position_dragons(dragons)
print(position_dragons(dragons))
dessine_donjon(donjon, dragons, aventurier)
dessine_aventurier(donjon, aventurier.position)
dessine_dragons(donjon, position_dragons(dragons))

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
        chemin = intention(donjon, position, dragons, [])
        for i in range(1, len(dragons)-1):
            dragon = dragons[i]
            new_chemin = intention(donjon, position, dragons)
            if dragon.niveau > donne_dragon(dragons, new_chemin[len(new_chemin)-1]).niveau:
                chemin = new_chemin
        dessine_chemin(donjon, chemin)
        print(donjon[0][4])

    elif tev == "Touche":
        nom_touche = touche(ev)

        if nom_touche == "space":
            # L'aventurier affronte le dragon
            if chemin != []:
                position = chemin[len(chemin)-1]
                for dragon in dragons:
                    if dragon.position == position:
                        dragon_affronte = dragon
                        break
                print("niveau dragon: ", dragon.niveau)
                if aventurier.niveau < dragon.niveau:
                    
                    print("PERDU")
                    break
                dragons = deplace_aventurier(aventurier, dragons, position)
                dessine_chemin(donjon, [])
                dessine_aventurier(donjon, position)
                dessine_dragons(donjon, position_dragons(dragons))
    mise_a_jour()
ferme_fenetre()
