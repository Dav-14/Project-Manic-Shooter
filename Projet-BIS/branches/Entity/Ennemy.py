import time
import os
import pygame
from pygame.locals import * 
import Entity.SpaceShip as _ss_

class EnnShip(_ss_.SpaceShip):
    def __init__(self, FCTposX, FCTposY, Pobj,style=1, __speed__ = 5, life=100, dmg=1, bullet_type="single_ennemy"):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        Type = "Ennemy_"
        super().__init__(life, dmg ,Type, style, __speed__,bullet_type)
        self.bullet_style = 41


        self.init_pos(FCTposX, FCTposY)
        self.posX, self.posY = self.rect.x, self.rect.y 

        self.FCTnewposXX = FCTnewposXX
        self.FCTnewposYY = FCTnewposYY

        self.break_btw_phase = None
        self.breaked = None
        self.patern_done = False
        self.phase = 0
        self.position = Pobj
        self.passiv = False #Si true ne pourra pas prendre de dégats

    def init_pos(self, FCTposX, FCTposY):

        self.rect.x = int(FCTposX(self.width, self.height, self.Surf_Width, self.Surf_Height))
        self.rect.y = int(FCTposY(self.width, self.height, self.Surf_Width, self.Surf_Height))

    def new_pos(self):

        self.posX = self.FCTnewposXX(self.posX, self.posY, self.width, self.height, self.angle, self.time, self.__speed__)
        self.posY = self.FCTnewposYY(self.posX, self.posY, self.width, self.height, self.angle, self.time, self.__speed__)

        self.rect.x = int(self.posX)
        self.rect.y = int(self.posY)

    def patern_executed(self):

        if self.posX <= (0 - 2*self.width)  or self.posX >= (self.Surf_Width + 2*self.width):
            self.patern_done = True
            self.passiv = True
            self.breaked = pygame.time.get_ticks()
        if self.posY <= (0 - 2*self.height) or self.posY >= (self.Surf_Height + 2*self.height):
            self.patern_done = True
            self.passiv = True
            self.breaked = pygame.time.get_ticks()


    def update(self):

        if not self.patern_done:
            self.new_pos()
            self.patern_executed()
        else:
            now = pygame.time.get_ticks()
            if now - self.breaked >= self.break_btw_phase:
                self.patern_done = False
                self.passiv = False
            
        if self.life == 0:
            self.kill()
        

    def shoot(self):
        pass