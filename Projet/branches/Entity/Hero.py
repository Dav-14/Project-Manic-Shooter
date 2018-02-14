import time
import os
import pygame
from pygame.locals import * 

class hero:

    def __init__(self, mv_cooldown = 200, style = "spaceCraft1.png"):
        self.mv_cooldown = mv_cooldown
        self.style = pygame.image.load(os.path.join("..","Ressources","Graphics","SpaceShip",style)).convert_alpha()
        #Constructeur
        self.width, self.height = self.style.get_width(), self.style.get_height()
        now = pygame.time.get_ticks()
        #############################
        #Pour faire des mouvements alterné
        self.last_move_top = now#Gere les déplacement tous les X cooldowns
        self.last_move_bottom = now
        self.last_move_left = now
        self.last_move_right = now#On est obligé de creer 4 variables si l'on veut faire des mouvements
        #############################

        self.posX = 0#Position en X du héro.
        self.posY = 0#Position en Y du héro.



    def haut(self, maGrille):#Permet de faire déplacer le héro vers la gauche.
        now = pygame.time.get_ticks()
        if (self.posY - 1 >= 0) and (now - self.last_move_top >= self.mv_cooldown):
            self.last_move_top = pygame.time.get_ticks() #Vérifie que la position ne depasse pas la grille en haut.
            self.last_move = pygame.time.get_ticks()
            self.posY -= 1#Lui donne une nouvelle direction

    def bas(self, maGrille):#Permet de faire se déplacer le héro sur la droite.
        now = pygame.time.get_ticks()
        if (self.posY + 1 < maGrille.ligne) and (now - self.last_move_bottom >= self.mv_cooldown):
            self.last_move_bottom = pygame.time.get_ticks()#Vérifie que la position ne dépasse pas la grille en bas.
            self.posY += 1#Lui donne une nouvelle direction

    def gauche(self, maGrille):
        now = pygame.time.get_ticks()
        if self.posX - 1 >= 0 and (now - self.last_move_left >= self.mv_cooldown):
            self.last_move_left = pygame.time.get_ticks() #On vérifie que la position future ne depasse pas la grille a gauche
            self.posX -= 1 #On change sa position

    def droite(self, maGrille):
        now = pygame.time.get_ticks()
        if self.posX + 1 < maGrille.colonne and (now - self.last_move_right >= self.mv_cooldown):
            self.last_move_right = pygame.time.get_ticks()
            self.posX += 1#On change sa position
