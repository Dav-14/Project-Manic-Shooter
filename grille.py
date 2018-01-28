import math
import os

class grille:

    def __init__(self, ligne, colonne):
        #Constructeur
        self.ligne = ligne
        self.colonne = colonne
        self.grid = []

    def creerGrille(self, val):
        #grid = []
        for i in range(self.ligne):#On parcours le nombres de ligne
            l = [val]*self.colonne#Ajoute à chaque tour de boucle la valeur à la ligne
            self.grid.append(l)#Ajoute la variable l à la grille.
        return self.grid#Retourne la grille.


    def affiche(self):
        os.system("clear")#Vide la console a chaque affichage
        #Affiche en mode console
        ch = ""#Créer une liste vide.

        for liste in self.grid:
            for c in liste:
                ch += str(c + 5*" ")
            ch += "\n\n"
        print(ch)

   

