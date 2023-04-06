from fltk import*
largeur, hauteur = 1000, 1000
k = (largeur + hauteur) // 2
k *= 1/5
cree_fenetre(largeur, hauteur)
image(0, 0, 'game_files/media/fond.png', tag="fond")

def dessine_donjon(donjon, dragons, aventurier):
    # dragons et aventurier sont ici compris comme des coordonnées
    for i in range(len(donjon)):
        for j in range(len(donjon[0])):
            salle = donjon[i][j]
            rectangle(i*k, j*k, i*k + k, j*k + k, epaisseur = 5)

donjon = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
for i in range(len(donjon)):
        for j in range(len(donjon[0])):
            salle = donjon[i][j]
            rectangle(i*k, j*k, i*k + k, j*k + k, epaisseur = k/3)