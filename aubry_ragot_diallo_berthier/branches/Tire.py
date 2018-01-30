from Grille import *
import Entity.Hero as mHero
import Entity.Ennemis as mEnnemis

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
    def collision(lTires, lEnnemis): #Test de collision, si oui on remplace l'objet par une chaine "del"
        for Tir in lTires:#On parcours pour tout les tir
            for Enn in lEnnemis:
                #if Tir isinstance (Tire,tire) and Enn isinstance (mEnnemis,ennemis):       
                if tir.posXTire == shoot.posX:
                    if tir.posY + 1 == enn.posY:
                        enn,tir = "del"
        if "del" in lEnnemis:#On test dans une liste OU l'autre car dans tous les cas si on a un "del", il y en aura forcement un dans l'autre
            supress_del(lTires)# On pourra réduire le mot del par la suite ou le garde en exclu.
            supress_del(lEnnemis)

    def supress_del(liste): #Suprime tout les del de la liste
        liste = [i for i in liste if i != "del"]


#OPTIMISER LE CODE TIRE/COLLISION/SUPRESS_DEL