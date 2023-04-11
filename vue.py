from fltk import*
img_dragon = "game_files/Dragon_s.png"
img_knight = "game_files/Knight_s.png"
img_treasure = "game_files/treasure.png"
fichier = open("parametres.txt", "r", encoding="utf-8")
parametres = fichier.read().splitlines()
largeur, hauteur = int(parametres[0]), int(parametres[1])
moyenne = (largeur + hauteur) // 2
k = moyenne/5
cree_fenetre(largeur, hauteur)
image(largeur//2, hauteur//2, 'game_files/media/fond.png', hauteur=1500, largeur=2000, tag="fond")

def dessine_donjon(donjon, dragons, aventurier):
    # dragons et aventurier sont ici compris comme des coordonnées
    for i in range(len(donjon)):
        for j in range(len(donjon[0])):
            x0, y0 = i * (largeur/len(donjon)), j * (hauteur/len(donjon[0]))
            x1, y1 = (i+1) * (largeur/len(donjon)), (j+1) * (hauteur/len(donjon[0]))
            salle = donjon[i][j]
            rectangle(x0, y0, x1, y1, tag=str(i)+str(j), epaisseur=k/3)
            for l in range(len(salle)):
                porte = salle[l]
                if porte:
                    if l == 0:
                        ligne(x0, y0, x0, y1, couleur="red", epaisseur=5, tag="p"+str(i)+str(j))
                    elif l == 1:
                        ligne(x1, y0, x1, y1, couleur="blue", epaisseur=5, tag="p"+str(i)+str(j))
                    elif l == 2:
                        ligne(x1, y1, x0, y1, couleur="green", epaisseur=5, tag="p"+str(i)+str(j))
                    elif l == 3:
                        ligne(x0, y1, x0, y0, couleur="yellow", epaisseur=5, tag="p"+str(i)+str(j))

# donjon = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
# for i in range(len(donjon)):
#         for j in range(len(donjon[0])):
#             salle = donjon[i][j]
#             rectangle(i*k, j*k, i*k + k, j*k + k, epaisseur = k/3)
