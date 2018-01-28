import os
try:
    import pygame
except ImportError:
    os.system("pip3 install pygame")

from grille import *
import Hero as mHero
import Ennemis as mEnnemis
import tire as mTire

pygame.init()

global colonne
global ligne
global val

error = True

def switch(value):
    if value == 0:
        return "Veuillez entrer des valeurs entières !"
    if value == "titre":
        return "Manic Shooter : Shot'em up !"
    return None

while error:
    try:
        ligne = int(input("La hauteur de votre grille ? \n"))
        colonne = int(input("La largeur de votre grille ? \n"))
    except ValueError:
        print(switch(0))
    else:
        while(colonne%2 == 0) or (colonne >= ligne):
            try:
                colonne = int(input("La largeur de votre grille doit être impaire et inferieur à " + str(ligne) + "\n"))
            except ValueError:
                print(switch(0))
            else:
                error = False
        error = False

fps = 60 #IPS ou Frame per seconds
Height = 800 #Hauteur
Width = 500 #Largeur
val = "-"

###################################
# DEFINITION DE LA GRILLE
maGrille = grille(ligne, colonne)
maGrille.creerGrille(val)
maGrille.affiche()
###################################
print(maGrille)
###################################
# CREATION DU HERO
monhero = mHero.hero()
monhero.ajoutHero(maGrille)
###################################
def waves(nb, listeEnnemis):
    
    if nb == "init":
        for i in range(5):
            ennemi = mEnnemis.ennemis()
            ennemi.ajoutEnnemis(listeEnnemis)
            listeEnnemis.append(ennemi)
    return listeEnnemis
###################################
# Initialisation de la première vague d'énnemie
listeEnnemis = []
listeEnnemis = waves("init", listeEnnemis)
###################################



maGrille.affiche() # Affichage de la grille avec ENNEMIE + HERO + VIDE

listeTire = [] #Liste qui va contenir les instances des tirs.
 #Liste qui va contenir les instances des ennemis.

Window = pygame.display.set_mode((Width,Height))
pygame.display.set_caption(switch("titre"))

continuer = True

while continuer:
    pygame.time.Clock().tick(fps)#Actualisation toutes les 5 frames
    for event in pygame.event.get():

        if event.type == pygame.QUIT:#Si on ferme la fenêtre
            continuer = False

        if event.type == pygame.KEYDOWN:#Si TOUCHE ENFONCE

            if event.key == pygame.K_ESCAPE:#Touche Echape
                continuer = False

            if event.key == pygame.K_SPACE:
                tir = mTire.tire(monhero)
                tir.tirer(maGrille)
                listeTire.append(tir)

            if event.key == pygame.K_UP:
                monhero.haut(maGrille)

            if event.key == pygame.K_DOWN:
                monhero.bas(maGrille)

            if event.key == pygame.K_LEFT:
                monhero.gauche(maGrille)

            if event.key == pygame.K_RIGHT:
                monhero.droite(maGrille)

            if len(listeTire) >= 1:
                for shoot in listeTire:
                    shoot.tire(maGrille, monennemis)
                    if shoot.posXTire == monennemis.posX:#Vérifie la collision entre l'ennemie et le tir.
                        maGrille.grid[tir.posXTire][tir.posYTire] = "-"#Remplace le tir par la val de défaut.
                        del shoot #####A FAIRE Suprimer l'instance de la liste
                        print(listeTire)
    pygame.display.update()
    maGrille.affiche()
pygame.quit()
quit()

