import time
import os
import pygame
import sympy as sp
from pygame.locals import *

class bullet(pygame.sprite.Sprite):
    def __init__(self, spaceShip, __dict_bullet, i):
        now = pygame.time.get_ticks()
        super().__init__()

        
        self.type = "Bullet_"
        self.style = str(spaceShip.bullet_style)
        self.image = pygame.image.load(os.path.join("..","Ressources","Graphics","Bullet",self.type + self.style + ".png")).convert_alpha()
        
        coef = (self.image.get_height())/(self.image.get_width())
        self.width = 5
        self.height = int(coef*self.width)

        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()

        self.position = i
        self.bullet_type = spaceShip.bullet_type

        dict_file = __dict_bullet["typ_bullet"][self.bullet_type]["position"][str(i)]
        FCTposX = sp.sympify(dict_file["x"])
        FCTposY = sp.sympify(dict_file["y"])

        self.angle = dict_file["angle"]
        self.image = pygame.transform.rotate(self.image, self.angle)
        #sp.pprint(self.trajectY)
        x, y, w, h, sw, sh, s, a = sp.symbols("x, y, w, h, sw, sw, s, a")

        self.rect.x = FCTposX.subs({x:spaceShip.posX, y:spaceShip.posY, sw:spaceShip.width, sh:spaceShip.height, w:self.width, h:self.height})
        self.rect.y = FCTposY.subs({x:spaceShip.posX, y:spaceShip.posY, sw:spaceShip.width, sh:spaceShip.height,w:self.width, h:self.height})
        
        self.speed___bullet = __dict_bullet["typ_bullet"][spaceShip.bullet_type]["speed"] #vitesse des balles, que l'on définira en Json les paramètres de base

        # TRAJECTOIRE
        dict_file = __dict_bullet["typ_bullet"][self.bullet_type]["fonction"][str(self.position)]
        self.FCTnewposX = sp.sympify(dict_file["x"])
        self.FCTnewposY = sp.sympify(dict_file["y"])

        #print(pygame.time.get_ticks() - now)

    def update(self,__dict_bullet):#A chaque frame change la position

        self.update_pos(__dict_bullet)
        self.auto_kill()
        
    def update_pos(self, __dict_bullet):
        now = pygame.time.get_ticks()
        x, y, w, h, s, a = sp.symbols("x, y, w, h, s, a")
        _dict = {x:self.rect.x, y:self.rect.y, w:self.width, h:self.height, s:self.speed___bullet, a:self.angle}
        self.rect.x = self.FCTnewposX.subs(_dict)
        self.rect.y = self.FCTnewposY.subs(_dict)
        #print("POS UP :", pygame.time.get_ticks()-now)
    def auto_kill(self):

        Surface = pygame.display.get_surface()
        Height, Width = Surface.get_height(), Surface.get_width()

        if self.rect.x >= Width + self.width or self.rect.x <= 0 - self.width:
            self.kill()
        if self.rect.y <= 0 - self.height or self.rect.y >= Height + self.height:
            self.kill()