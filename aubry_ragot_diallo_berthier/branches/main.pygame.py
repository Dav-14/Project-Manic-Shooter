import os
try:
    import pygame
except ImportError:
    os.system("pip3 install pygame")

from Grille import *
import Entity.Hero as mHero
import Entity.Ennemis as mEnnemis
import Tire as mTire

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

fps = 30 #IPS ou Frame per seconds
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
            ennemi.ajoutEnnemis(listeEnnemis, maGrille)
            listeEnnemis.append(ennemi)
    return listeEnnemis
###################################
# Initialisation de la première vague d'énnemie
listeEnnemis = []
listeEnnemis = waves("init", listeEnnemis)
###################################
###################################
# Menu PAUSE
def PAUSE():
    pauseGrid = grille(ligne,colonne)
    pauseGrid.creerGrille(val)
    pauseGrid.grid[0] = "PAUSE"
    pauseGrid.affiche()
    pygame.time.delay(5000)
    





maGrille.affiche() # Affichage de la grille avec ENNEMIE + HERO + VIDE

listeTire = [] #Liste qui va contenir les instances des tirs.
 #Liste qui va contenir les instances des ennemis.

Window = pygame.display.set_mode((Width,Height))
pygame.display.set_caption(switch("titre"))

continuer = True

#Pre_game_Menu test
def Menu():
    Pre_game_Menu = True
    keys = []
    while Pre_game_Menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_mods()
                print(key)
                pygame.display.update()
                if event.key == pygame.K_ESCAPE:
                    preset = False

#Fin preset test

flags = [0,0,0,0,0]
now = pygame.time.get_ticks()
while continuer:
    maGrille.affiche()
    pygame.time.Clock().tick(fps)#Actualisation toutes les 5 frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Si on ferme la fenêtre en cliquant sur la CROIX
            continuer = False
        if event.type == pygame.KEYDOWN:#Si TOUCHE ENFONCE
            if event.key == pygame.K_ESCAPE:#Touche Echape
                PAUSE()
            if event.key == pygame.K_SPACE:#Touche Espace
                flags[0] = 1
            if event.key == pygame.K_UP:
                flags[1] = 1
            if event.key == pygame.K_DOWN:
                flags[2] = 1
            if event.key == pygame.K_LEFT:
                flags[3] = 1
            if event.key == pygame.K_RIGHT:
                flags[4] = 1
        if event.type == pygame.KEYUP:#Si touche RELACHE
            if event.key == pygame.K_SPACE:#Touche Espace
                flags[0] = 0
            if event.key == pygame.K_UP:
                flags[1] = 0
            if event.key == pygame.K_DOWN:
                flags[2] = 0
            if event.key == pygame.K_LEFT:
                flags[3] = 0
            if event.key == pygame.K_RIGHT:
                flags[4] = 0
    #EN FONCTION DES TOUCHES UTILISE
    if flags[0] == 1:
        tir = mTire.tire(monhero)
        tir.tirer(maGrille)
        listeTire.append(tir)
    if flags[1] == 1:
        monhero.haut(maGrille)
    if flags[2] == 1:
        monhero.bas(maGrille)
    if flags[3] == 1:
        monhero.gauche(maGrille)
    if flags[4] == 1:
        monhero.droite(maGrille)
    if len(listeTire) >= 1:
        #GERER CETTE PARTIE DANS TIRE DIFFERAMENT, ALGORITHME SIMPLIFIABLE.
        for tir in listeTire:
             tir.tire(maGrille)
        Tire.collision(listeTire,listeTire)
    pygame.display.update()
    maGrille.affiche()
pygame.quit()
quit()

