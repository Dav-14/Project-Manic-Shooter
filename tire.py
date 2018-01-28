from grille import *
import Hero as mHero
import Ennemis as mEnnemis

class tire:

    def __init__(self, hero):
        #Constructeur
        self.posX = hero.posX#Position en X du héro.
        self.posY = hero.posY#Position en Y du héro.
        self.posXTire = 0#Position en X du tire.
        self.posYTire = 0#Position en Y du tire.

    def tirer(self, maGrille):
        self.posXTire = self.posX - 1 #Défini la position en X du tire.
        self.posYTire = self.posY#Défini la postion en Y du tire.
        maGrille.grid[self.posXTire][self.posYTire] = "|"#Place le tire.

    def tire(self, maGrille, ennemis):

        #Si le tire dépasse la hauteur de la grille il vaut "-".
        if self.posXTire == 0:
            maGrille.grid[self.posXTire][self.posYTire] = "-"#Remplace l'ancienne position par un nul.

        #Si le tire touche un "0" alors la position du tire vaut désormais la position du zéro et le tire disparrait.
        #Il est remplacé par un "-"

        if self.posXTire == ennemis.posX:
            ennemis.posX = "-"
            self.posXTire += 1#Décremente la position actuelle.
            maGrille.grid[self.posXTire][self.posYTire] = "-"#Remplace l'ancienne position par un nul.

        #Déroule le tire correctement.
        else:
            maGrille.grid[self.posXTire][self.posYTire] = "-"#Remplace l'ancienne position par un nul.
            self.posXTire -= 1#Décremente la position actuelle.
            maGrille.grid[self.posXTire][self.posYTire] = "|"#Réajuste la position du tire.
