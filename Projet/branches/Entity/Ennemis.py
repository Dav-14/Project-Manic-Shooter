import math
import random as rd

class ennemis:#Class qui définit un ennemi.

    def __init__(self, style=None):#Constructeur de la class.
        self.posX = 0#Position X de départ.
        self.posY = 0#Position Y de départ.
        if style == None:
            self.style = "0"
        else:
            self.style = style

    def rd_POS(self,colonneGrille):#Ajoute une position random à un ennemis.
        return rd.randint(0,1),rd.randint(0,(colonneGrille - 1))#Utilise la fonction randint permettant de mettre aléatoire.

    def ajoutEnnemis(self, dictEnnemis, maGrille): #Permet l'ajout d'un ennemis de façon aléatoire.
        #A ajouter
        print(dictEnnemis)
        if len(dictEnnemis) >= 1:
            lPosEnnemis = []
            for enn in dictEnnemis.values():
                lPosEnnemis.append([enn.posX, enn.posY])

            posX, posY = self.rd_POS(maGrille.colonne)  #Initialisation de position potentiel d'un nouvel ennemi.

            while [posX,posY] in lPosEnnemis:   #Vérification s'il en existe pas un de present sur les positions générés
                posX, posY = self.rd_POS(maGrille.colonne)
        else:
            posX, posY = self.rd_POS(maGrille.colonne)

        print(posX,posY)
        print(maGrille.grid[posX][posY])

        self.posX = posX#Définit la position de l'ennemi en X par rapport à la variable posX.
        self.posY = posY#Définit la position de l'ennemi en Y par rapport à la variable posY.

        maGrille.grid[self.posX][self.posY] = self.style #Ajoute un ennemis de façon aléatoire dans le haut de la grille.

    def defile(self,maGrille):#Fait défiler un ennemi vers le bas.
    #A COMPLETER
        if self.posX  == maGrille.colonne:#Vérifie que l'ennemis ne dépasse pas la hauteur.
            maGrille.grid[self.posX][self.posY] = "-"#Si c'est le cas alors on le suprime.
