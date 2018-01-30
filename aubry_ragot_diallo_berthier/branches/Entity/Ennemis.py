import math
import random as rd

def rd_POS(y):
    return rd.randint(0,1),rd.randint(0,(y - 1))


class ennemis:

    def __init__(self):
        self.posX = 0
        self.posY = 0

    def ajoutEnnemis(self, lEnnemis, maGrille): #Permet l'ajout d'un ennemis de façon aléatoire.
        #A ajouter
        c_enn = "0"

        if len(lEnnemis) >= 1:
            lPosEnnemis = []
            for enn in lEnnemis:
                lPosEnnemis.append([enn.posX, enn.posY])

            posX, posY = rd_POS(maGrille.colonne)  #Initialisation de position potentiel d'un nouvel ennemi

            while [posX,posY] in lPosEnnemis:   #Vérification s'il en existe pas un de present sur les positions générés
                posX, posY = rd_POS(maGrille.colonne)
        else:
            posX, posY = rd_POS(maGrille.colonne)

        print(posX,posY)
        print(maGrille.grid[posX][posY])

        self.posX = posX
        self.posY = posY        

        maGrille.grid[self.posX][self.posY] = c_enn #Ajoute un ennemis de façon aléatoire dans le haut de la grille.

    def defile(self,maGrille):
        if self.posX  == maGrille.colonne:#Vérifie que l'ennemis ne dépasse pas la hauteur.
            maGrille.grid[self.posX][self.posY] = "-"#Si c'est le cas alors on le suprime.



    def collision(self):

        return None
