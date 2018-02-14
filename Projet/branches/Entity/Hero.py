import time
import os
import pygame
from pygame.locals import * 

class hero:

    def __init__(self, mv_cooldown = 20, style = "spaceCraft1.png", size=None, __vect_v = 5):

        Surface = pygame.display.get_surface()#Recupere la surface de la fenetre
        Width, Height = Surface.get_width(), Surface.get_height()#Recupere sa longeur et largeur

        self.mv_cooldown = mv_cooldown
        self.__vect_v = __vect_v

        self.style = pygame.image.load(os.path.join("..","Ressources","Graphics","SpaceShip",style)).convert_alpha()#Charge l'image
        self.width, self.height = self.style.get_width(), self.style.get_height()#Défini la Résolution affiché de notre objet

        self.coef = (self.height)/(self.width)#Calcul le coef de proportion de l'objet
        self.width = int(1/10*Width)#On les tailles de la résolution de l'image
        self.height = int(self.coef * self.width)
        self.style = pygame.transform.scale(self.style, (self.width,self.height))#Puis on appliques les nouvelles proportion

        now = pygame.time.get_ticks()
        #############################
        #Pour faire des mouvements alterné
        self.last_move_top = now#Gere les déplacement tous les X cooldowns
        self.last_move_bottom = now
        self.last_move_left = now
        self.last_move_right = now#On est obligé de creer 4 variables si l'on veut faire des mouvements
        #############################
        self.posX = Width/2 - self.width/2
        self.posY = Height*(1-(5/80)) - self.height

    def haut(self):#Permet de faire déplacer le héro vers la gauche.
        now = pygame.time.get_ticks()
        if self.posY != 0:
            if self.posY - self.__vect_v < 0:
                self.posY = 0
            else:
                self.posY -= self.__vect_v
                        

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
