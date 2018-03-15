import time
import os
import pygame
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy.abc import x, y, s, a, t, w, h, c, v

from pygame.locals import *


def loader_fct_bullet(__dict_bullet):
    for i in __dict_bullet["typ_bullet"]: 
        for j in __dict_bullet["typ_bullet"][i]["position"]:
        
            Fct1 = lambdify((x, y, w, h, c, v), sp.sympify(__dict_bullet["typ_bullet"][i]["position"][j]["x"]), modules=["math"])
            Fct2 = lambdify((x, y, w, h, c, v), sp.sympify(__dict_bullet["typ_bullet"][i]["position"][j]["y"]), modules=["math"])

            __dict_bullet["typ_bullet"][i]["position"][j]["x"]= Fct1
            __dict_bullet["typ_bullet"][i]["position"][j]["y"]= Fct2
        
        for j in __dict_bullet["typ_bullet"][i]["fonction"]:
            
            Fct1 = lambdify((x, y, s, a, t), sp.sympify(__dict_bullet["typ_bullet"][i]["fonction"][j]["x"]), modules=["math"])
            Fct2 = lambdify((x, y, s, a, t), sp.sympify(__dict_bullet["typ_bullet"][i]["fonction"][j]["y"]), modules=["math"])

            __dict_bullet["typ_bullet"][i]["fonction"][j]["x"]= Fct1
            __dict_bullet["typ_bullet"][i]["fonction"][j]["y"]= Fct2

    return __dict_bullet

class bullet(pygame.sprite.Sprite):
    def __init__(self, spaceShip, __dict_bullet, i):
        super().__init__()

        self.type = "Bullet_"
        self.bullet_type = spaceShip.bullet_type
        self.style = str(spaceShip.bullet_style)
        self.image = pygame.image.load(os.path.join("..","Ressources","Graphics","Bullet",self.type + self.style + ".png")).convert_alpha()

        coef = (self.image.get_height())/(self.image.get_width())
        self.width = 5
        self.height = int(coef*self.width)

        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = self.image.get_rect()

        self.position = i

        dict_file = __dict_bullet["typ_bullet"][self.bullet_type]["position"][str(self.position)]
        self.angle = dict_file["angle"]
        self.image = pygame.transform.rotate(self.image, self.angle)

        self.init_pos(dict_file, spaceShip)
        
        self.FposX = self.rect.x 
        self.FposY = self.rect.y
        # TRAJECTOIRE
        dict_file = __dict_bullet["typ_bullet"][self.bullet_type]["fonction"][str(self.position)]

        #self.FCTnewposXX = lambdify((x, y, s, a, t), sp.sympify(dict_file["x"]), modules=["math"])
        #self.FCTnewposYY = lambdify((x, y, s, a, t), sp.sympify(dict_file["y"]), modules=["math"])

        self.FCTnewposXX = dict_file["x"]
        self.FCTnewposYY = dict_file["y"]

        self.speed___bullet = __dict_bullet["typ_bullet"][spaceShip.bullet_type]["speed"] #vitesse des balles, que l'on définira en Json les paramètres de base
        self.time = 0

    def init_pos(self, dict_file, spaceShip):
        
        #FCTposX = lambdify((x, y, w, h, c, v), sp.sympify(dict_file["x"]), modules=["math"])

        #FCTposY = lambdify((x, y, w, h, c, v), sp.sympify(dict_file["y"]), modules=["math"])

        FCTposX = dict_file["x"]
        FCTposY = dict_file["y"]

        self.rect.x = FCTposX(spaceShip.rect.x, spaceShip.rect.y, self.width, self.height, spaceShip.width, spaceShip.height)
        self.rect.y = FCTposY(spaceShip.rect.x, spaceShip.rect.y, self.width, self.height, spaceShip.width, spaceShip.height)

    def update(self, __dict_bullet, delta_time):  # A chaque frame change la position

        self.time += delta_time
        self.update_pos(__dict_bullet)
        self.auto_kill()

    def update_pos(self, __dict_bullet):

        self.FposX = self.FCTnewposXX(self.FposX, self.FposY, self.speed___bullet,
                                       self.angle, self.time)

        self.FposY = self.FCTnewposYY(self.FposX, self.FposY, self.speed___bullet,
                                       self.angle, self.time)

        self.rect.x = int(self.FposX)
        self.rect.y = int(self.FposY)
        #print("POS : ",self.position + 1 ,"X =", self.rect.x, "Y =", self.rect.y)

    def auto_kill(self):

        Surface = pygame.display.get_surface()
        Height, Width = Surface.get_height(), Surface.get_width()

        if self.rect.x >= Width + self.width or self.rect.x <= 0 - self.width:
            self.kill()
        if self.rect.y <= 0 - self.height or self.rect.y >= Height + self.height:
            self.kill()