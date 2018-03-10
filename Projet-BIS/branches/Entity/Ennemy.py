import time
import os
import pygame
from pygame.locals import * 
import Entity.SpaceShip as _ss_

class EnnShip(_ss_.SpaceShip):
    def __init__(self,style=1, __speed__ = 5, hp=100, dmg=1):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        Type = "Ennemy_"
        super().__init__(Type, style, __speed__)
        self.hp = hp
        self.dmg = dmg
    
    def update(self):
        pass
    