from grille import *

class hero:

    def __init__(self):
        #Constructeur
        self.posX = 0#Position en X du héro.
        self.posY = 0#Position en Y du héro.
        self.c_Hero = "1"#Un hero vaut le chiffre 1.

    def ajoutHero(self, maGrille): #Permet l'ajout du héro.

        self.posY = maGrille.ligne - 1 #On obtient les coordonnees Y
        self.posX = int(maGrille.colonne/2) #On obtient les coordonnees X du hero.
        maGrille.grid[self.posY][self.posX] = self.c_Hero # ajout du hero dans le centre de la liste


    def haut(self, maGrille):#Permet de faire déplacer le héro vers la gauche.
        if self.posY - 1 >= 0: #Vérifie que la position ne depasse pas la grille en haut
            maGrille.grid[self.posY][self.posX] = "-"#Remplace la position precedente
            self.posY -= 1#Lui donne une nouvelle direction
            maGrille.grid[self.posY][self.posX] = self.c_Hero#Applique la direction

    def bas(self, maGrille):#Permet de faire se déplacer le héro sur la droite.

        if self.posY + 1 < maGrille.ligne:#Vérifie que la position ne dépasse pas la grille en bas.
            maGrille.grid[self.posY][self.posX] = "-"#Remplace la position precedente
            self.posY += 1#Lui donne une nouvelle direction
            maGrille.grid[self.posY][self.posX] = self.c_Hero#Applique la direction

    def gauche(self, maGrille):
        if self.posX - 1 >= 0: #On vérifie que la position future ne depasse pas la grille a gauche
            maGrille.grid[self.posY][self.posX] = "-"
            self.posX -= 1 #On change sa position
            maGrille.grid[self.posY][self.posX] = self.c_Hero #On "ecrit" sa positons dans la grille

    def droite(self, maGrille):
        if self.posX + 1 < maGrille.colonne:
            c_Hero = "1"#On vérifie que la position future ne depasse pas la grille a droite
            maGrille.grid[self.posY][self.posX] = "-"
            self.posX += 1#On change sa position
            maGrille.grid[self.posY][self.posX] = c_Hero#On "ecrit" sa positons dans la grille