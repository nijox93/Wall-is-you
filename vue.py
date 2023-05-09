from fltk import*
img_dragon = "game_files/Dragon_s.png"
img_knight = "game_files/Knight_s.png"
img_treasure = "game_files/treasure.png"
fichier = open("parametres.txt", "r", encoding="utf-8")
parametres = fichier.read().splitlines()
largeur, hauteur = int(parametres[0]), int(parametres[1])
moyenne = (largeur + hauteur) // 2
k = moyenne/25
cree_fenetre(largeur, hauteur)
rectangle(0, 0, largeur, hauteur, remplissage="white")
# image(largeur//2, hauteur//2, 'game_files/media/fond.png', hauteur=1500, largeur=2000, tag="fond")

def dessine_donjon(donjon, dragons, aventurier):
    # dragons et aventurier sont ici compris comme des coordonnées
    for i in range(len(donjon)):
        for j in range(len(donjon[0])):
            x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
            x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
            salle = donjon[i][j]
            rectangle(x0, y0, x1, y1, tag=str(i)+str(j), epaisseur=k)
    for i in range(len(donjon)):
        for j in range(len(donjon[0])):
            x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
            x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
            salle = donjon[i][j]
            n = 0
            for porte in salle:
                if porte == True:
                    if n == 0:
                        rectangle(x0+k, y0, x1-k, y0+k, couleur="white", remplissage="white", tag="p0"+str(i)+str(j))
                    elif n == 1:
                        rectangle(x1, y0+k, x1-k, y1-k, couleur="white", remplissage="white", tag="p1"+str(i)+str(j))
                    elif n == 2:
                        rectangle(x1-k, y1, x0+k, y1-k, couleur="white", remplissage="white", tag="p2"+str(i)+str(j))
                    elif n == 3:
                        rectangle(x0, y1-k, x0+k, y0+k, couleur="white", remplissage="white", tag="p3"+str(i)+str(j))
                n += 1
    
def dessine_portes(donjon, position):
    (i,j) = position
    x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
    x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
    n = 0
    for porte in donjon[i][j]:
        if porte:
            couleur = "white"
            if n == 0:
                rectangle(x0+k, y0, x1-k, y0+k, couleur=couleur, remplissage=couleur, tag="p0"+str(i)+str(j))
            elif n == 1:
                rectangle(x1, y0+k, x1-k, y1-k, couleur=couleur, remplissage=couleur, tag="p1"+str(i)+str(j))
            elif n == 2:
                rectangle(x1-k, y1, x0+k, y1-k, couleur=couleur, remplissage=couleur, tag="p2"+str(i)+str(j))
            elif n == 3:
                rectangle(x0, y1-k, x0+k, y0+k, couleur=couleur, remplissage=couleur, tag="p3"+str(i)+str(j))
        else:
            efface("p"+str(n)+str(i)+str(j))
        n += 1

def dessine_image(donjon, position, path, tag):
    (i,j) = position
    x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
    x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
    image(x0 + (x1 - x0)//2, y0 + (y1 - y0)//2, path, hauteur=int(k*2), largeur=int(k*2), tag=tag)

def dessine_aventurier(donjon, position):
    efface("aventurier")
    dessine_image(donjon, position, "game_files/media/pikachu.png", "aventurier")

def dessine_dragons(donjon, pos_dragons):
    ''' Dessine des dragons '''
    efface("dragon")
    for position in pos_dragons:
        dessine_image(donjon, position, "game_files/media/gengar2.png", "dragon")

def dessine_chemin(donjon, chemin):
    efface("chemin")
    if chemin != []:
        n = 0
        while n != len(chemin)-1:
            (i,j) = chemin[n]
            x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
            x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
            xf_1, yf_1 = x0 + (x1 - x0)//2, y0 + (y1 - y0)//2
                
            (i,j) = chemin[n+1]
            x0, y0 = j * (largeur/len(donjon)), i * (hauteur/len(donjon[0]))
            x1, y1 = (j+1) * (largeur/len(donjon)), (i+1) * (hauteur/len(donjon[0]))
            xf_2, yf_2 = x0 + (x1 - x0)//2, y0 + (y1 - y0)//2
            
            ligne(xf_1, yf_1, xf_2, yf_2, 'red', k/3, tag="chemin")
            n += 1

def donne_position(donjon, abscisse, ordonnee):
    ''' Renvoie la case correspondant au couple de coordonnées abscisse/ordonnée '''
    return int(abscisse // (largeur/len(donjon[0]))), int(ordonnee // (hauteur/len(donjon)))
