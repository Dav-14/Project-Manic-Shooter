from grille import *
import math
import random

class ennemis:

    def __init__(self):
        self.posX = 0
        self.posY = 0

    def ajoutEnnemis(self, lEnnemis): #Permet l'ajout d'un ennemis de façon aléatoire.
        #A ajouter
        ennemis = "0"

        if len(lEnnemis) >= 1:
            lPosEnnemis = []
            for enn in lEnnemis:
                lPosEnnemis.append([enn.posX, enn.posY])

            posX = math.ceil(random.random()*2)-1 #Initialisation de position potentiel d'un nouvel ennemi
            posY = math.ceil(random.random()*maGrille.ligne)-1

            while [posX,posY] in lPosEnnemis:   #Vérification s'il en existe pas un de present sur les positions générés
                posX = math.ceil(random.random()*2)-1
                posY = math.ceil(random.random()*maGrille.ligne)-1
        else:
            posX = math.ceil(random.random()*2)-1
            posY = math.ceil(random.random()*maGrille.ligne)-1

        self.posX = posX
        self.posY = posY        

        maGrille.grid[self.posX][self.posY] = ennemis#Ajoute un ennemis de façon aléatoire dans le haut de la grille.


    def defile(self,maGrille):
        if self.posX  == maGrille.colonne:#Vérifie que l'ennemis ne dépasse pas la hauteur.
            maGrille.grid[self.posX][self.posY] = "-"#Si c'est le cas alors on le suprime.



    def collision(self):

        return None
