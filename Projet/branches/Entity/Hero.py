import time
import os
import pygame
from pygame.locals import * 

class hero:

    def __init__(self, style = "spaceCraft1.png", __vect_v = 10):

        Surface = pygame.display.get_surface()#Recupere la surface de la fenetre
        self.Surf_Width, self.Surf_Height = Surface.get_width(), Surface.get_height()#Recupere sa longeur et largeur

        self.__vect_v = __vect_v

        self.style = pygame.image.load(os.path.join("..","Ressources","Graphics","SpaceShip",style)).convert_alpha()#Charge l'image
        self.width, self.height = self.style.get_width(), self.style.get_height()#Défini la Résolution affiché de notre objet

        self.coef = (self.height)/(self.width)#Calcul le coef de proportion de l'objet
        self.width = int(1/10*self.Surf_Width)#On les tailles de la résolution de l'image
        self.height = int(self.coef * self.width)
        self.style = pygame.transform.scale(self.style, (self.width,self.height))#Puis on appliques les nouvelles proportion
        #############################
        self.posX = self.Surf_Width/2 - self.width/2
        self.posY = self.Surf_Height*(1-(5/80)) - self.height

    def up(self):#Permet de faire déplacer le héro vers la gauche.
        if self.posY != 0:
            if self.posY - self.__vect_v < 0:
                self.posY = 0
            else:
                self.posY -= self.__vect_v
                        

    def down(self):#Permet de faire se déplacer le héro sur la droite.
        if self.posY != self.Surf_Height - self.height:
            if self.posY + self.__vect_v > self.Surf_Height - self.height:
                self.posY = self.Surf_Height - self.height
            else:
                self.posY += self.__vect_v
                        

    def left(self):
        if self.posX != 0:
            if self.posX - self.__vect_v < 0:
                self.posX = 0
            else:
                self.posX -= self.__vect_v

    def right(self):
        if self.posX != self.Surf_Width - self.width:
            if self.posX + self.__vect_v > self.Surf_Width - self.width:
                self.posX = self.Surf_Width - self.width
            else:
                self.posX += self.__vect_v
