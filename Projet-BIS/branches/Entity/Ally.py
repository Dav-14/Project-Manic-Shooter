import time
import os
import pygame
from pygame.locals import * 
import Entity.SpaceShip as _ss_

class allyShip(_ss_.SpaceShip):
    def __init__(self, style=1, __speed__ = 10,bullet_type = "single", life = 100, dmg = 10):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        Type = "SpaceShip"
        super().__init__(Type, style, __speed__, bullet_type)
        self.life = life
        self.dmg = dmg
        self.bullet_style = 1

    def up(self):#Permet de faire déplacer le héro vers la gauche.
        if self.posY != 0:
            if self.posY - self.__speed__ < 0:
                self.posY = 0
            else:
                self.posY -= self.__speed__
            #self.Reactor.follow(self)
                       

    def down(self):#Permet de faire se déplacer le héro sur la droite.
        if self.posY != self.Surf_Height - self.height:
            if self.posY + self.__speed__ > self.Surf_Height - self.height:
                self.posY = self.Surf_Height - self.height
            else:
                self.posY += self.__speed__
            #self.Reactor.follow(self)


    def left(self):
        if self.posX != 0:
            if self.posX - self.__speed__ < 0:
                self.posX = 0
            else:
                self.posX -= self.__speed__
            #self.Reactor.follow(self)


    def right(self):
        if self.posX != self.Surf_Width - self.width:
            if self.posX + self.__speed__ > self.Surf_Width - self.width:
                self.posX = self.Surf_Width - self.width
            else:
                self.posX += self.__speed__
            #self.Reactor.follow(self)

    def update_style(self, style):
        pass