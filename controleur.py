from modele import*
from vue import*

#INITIALISATION
f = "game_files/maps/map_test.txt"
# f = open("game_files/maps/map_test.txt", "r", encoding="utf-8")
donjon, position, dragons = charge_fichier(f)
pos_dragons = position_dragons(dragons)
aventurier = Aventurier(position, 1)
print(intention(donjon, position, pos_dragons))
dessine_donjon(donjon, dragons, aventurier)
while(True):
    attend_ev()
    i, j = 2, 1
#     pivoter(donjon, (i, j))
#     dessine_portes(donjon, (i, j))
    for i in range(5):
        for j in range(2):
            pivoter(donjon, (i, j))
            dessine_portes(donjon, (i, j))
    print(donjon[2][1])
    
