import time
import os
import pygame
from pygame.locals import *

class reactor_f:
    def __init__(self, spaceShip):
        #self.spaceShip_type = spaceShip.type

        self.reactor_style = pygame.image.load(os.path.join("..","Ressources","Graphics","Reactor","Reactor_" + style)).convert_alpha()
        self.reactor_width, self.reactor_height = self.reactor_style.get_width(), self.reactor_style.get_height()
        
        self.reactor_coef = (self.reactor_height)/(self.reactor_width)
        self.reactor_width = int(6/12*spaceShip.width)
        self.reactor_height = int(self.reactor_coef*self.reactor_width)

        self.reactor_style = pygame.transform.scale(self.reactor_style, (self.reactor_width,self.reactor_height))
        self.reactor_posX = spaceShip.posX + spaceShip.width/2 - self.reactor_width/2
        self.reactor_posY = spaceShip.posY + spaceShip.height

    def follow(self, spaceShip):
        self.reactor_posX = spaceShip.posX + spaceShip.width/2 - self.reactor_width/2
        self.reactor_posY = spaceShip.posY + spaceShip.height - 1

