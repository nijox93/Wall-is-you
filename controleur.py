from modele import*

#INITIALISATION
f = "game_files/maps/map_test.txt"
# f = open("game_files/maps/map_test.txt", "r", encoding="utf-8")
donjon, position, dragons = charge_fichier(f)
pos_dragons = position_dragons(dragons)
aventurier = Aventurier(position, 1)
print(intention(donjon, aventurier.position, position_dragons(dragons)))