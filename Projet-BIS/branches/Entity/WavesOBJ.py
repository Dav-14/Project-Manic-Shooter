import time
import os
import pygame
import random as rd
from pygame.locals import * 
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy.abc import x, y, s, a, t, w, h, c, v

import Entity.EntityGroup as ENTGroup
import Entity.Ennemy as Enn

def loader_patern(_dict_Patern):
    #x = self.rect.x position actuelle de l'objet en x
    #y = self.rect.y position actuelle en y
    #w = self.width largeur de notre objet en pixels
    #h = self.height hauteur de notre obj
    #a = self.angle l'angle de rotation de l'image
    #s = self.__speed__ pour la vitesse des ennemis
    #c = self.Surf_Width la largeur de la fenetre
    #v = self.Surf_Height la hauteur de la fenetre
    for i in _dict_Patern["patern"]: 
        for j in _dict_Patern["patern"][i]["position"]:
            for k in _dict_Patern["patern"][i]["position"][j]:

                Fct1 = lambdify((w, h, c, v), sp.sympify(_dict_Patern["patern"][i]["position"][j][k]["x"]), modules=["math"])
                Fct2 = lambdify((w, h, c, v), sp.sympify(_dict_Patern["patern"][i]["position"][j][k]["y"]), modules=["math"])

                _dict_Patern["patern"][i]["position"][j][k]["x"] = Fct1
                _dict_Patern["patern"][i]["position"][j][k]["y"] = Fct2
    
        for j in _dict_Patern["patern"][i]["fonction"]:
            for k in _dict_Patern["patern"][i]["fonction"][j]:

                Fct1 = lambdify((x, y, w, h, a, t, s), sp.sympify(_dict_Patern["patern"][i]["fonction"][j][k]["x"]), modules=["math"])
                Fct2 = lambdify((x, y, w, h, a, t, s), sp.sympify(_dict_Patern["patern"][i]["fonction"][j][k]["y"]), modules=["math"])

                _dict_Patern["patern"][i]["fonction"][j][k]["x"] = Fct1
                _dict_Patern["patern"][i]["fonction"][j][k]["y"] = Fct2
        
    for i in _dict_Patern["ennemy_wave"]["fonction"]:
        Fct = lambdify((v), sp.sympify(_dict_Patern["ennemy_wave"]["fonction"][i]), modules=["math"])
        _dict_Patern["ennemy_wave"]["fonction"][i]= Fct
    return(_dict_Patern)

class Waves():
    def __init__(self, _dict_Patern):
        self._dict_ = _dict_Patern

        self._proba_l = {}
        self.items = []
        self.patern = None
        self.patern_duration = None

        self.wave = 1#On commence par la première wave
        self.wave_i = 0
        self.wave_FCT = self._dict_["ennemy_wave"]["fonction"][str(self.wave_i)]
        self.wave_change = None

        self.phase = 0

        self.end_patern = False
        self.Pause = False

        self.first_press_key = False
        self.start = 5000
        self.begin = None

        self.__GroupBullet_Ennemy = ENTGroup.Entity()
        self.__GroupSHIP = ENTGroup.Entity()
        
        self.numbers_ennemy = 0
        self.Cooldown_ennemy = 0
        self.last_ennemy_spawn = 0

        self.numbers_ennemy_init()
        self.patern_choose()

    def innit_prob(self):

        j = 0
        for i in self._dict_["patern"]:
            self.items.append(i)
            p = self._dict_["patern"][i]["Appears"]["Chance"]
            self._proba_l[str(j)]=p
            j+=1

    def proba_up_low(self):
        self._dict_["patern"][self.patern]["Appears"]["Chance"] += self._dict_["patern"][self.patern]["Appears"]["lower"]

        for i in self._dict_["patern"]:
            if i != self.patern:
                self._dict_["patern"][i]["Appears"]["Chance"] += self._dict_["patern"][self.patern]["Appears"]["upgrade"]

    def patern_choose(self):
        self.innit_prob()
        somme = 0
        
        for i in self._proba_l:#On fait la somme de toute les probabilité
            somme += self._proba_l[str(i)]
        x = rd.uniform(0,somme)

        for i in range(len(self._proba_l)):#On calcule retiens le patern qui va annuler le x choisi entre 0 et la somme
            x -= self._proba_l[str(i)]
            if x<=0:
                tmp = i
        
        self.patern = self.items[tmp]#Le patern choisi aura sa probabilité réduite, les autres auront leur probabilité augmenté
        self.proba_up_low()

        self.patern_duration = len(self._dict_["patern"][self.patern]["position"])

    def init_one_ennemy(self, pos):

        FCTposX = self._dict_["patern"][self.patern]["position"][str(self.phase)][str(pos)]["x"]
        FCTposY = self._dict_["patern"][self.patern]["position"][str(self.phase)][str(pos)]["x"]
        CalcposX = self._dict_["patern"][self.patern]["fonction"][str(self.phase)][str(pos)]["x"]
        CalcposY = self._dict_["patern"][self.patern]["fonction"][str(self.phase)][str(pos)]["x"]

        Ennemy = Enn.EnnShip(FCTposX,FCTposY,CalcposX,CalcposY,pos)
        self.__GroupSHIP.add(Ennemy)

        self.numbers_ennemy -= 1

    def wave_change_init(self):
        if len(self._dict_["ennemy_wave"]["fonction"]) > 1:
            self.wave_change = self._dict_["ennemy_wave"]["Wave change"][self.wave_i+1]
        else:
            self.wave_change = self._dict_["ennemy_wave"]["Wave change"][self.wave_i]

    def numbers_ennemy_init(self):
        self.wave_change_init()

        if self.wave == self.wave_change:
            if len(self._dict_["ennemy_wave"]["fonction"])>= self.wave_i +1:
                self.wave_i += 1
            self.wave_FCT = self._dict_["ennemy_wave"]["fonction"][str(self.wave_i)]

        self.numbers_ennemy = self.wave_FCT(self.wave)


    def ennemy_init(self):

        for i in range(int(self._dict_["patern"][self.patern]["Appears"]["PO"])):
            self.init_one_ennemy(i)
        self.last_ennemy_spawn = pygame.time.get_ticks()

    def phase_statement(self):

        for Sprite_obj in self.__GroupSHIP.sprites():
            if Sprite_obj.phase_done:
                Sprite_obj.break_btw_phase = self._dict_["patern"][self.patern]["times_break"][str(Sprite_obj.position)][str(Sprite_obj.phase)]
                if Sprite_obj.phase < self.patern_duration-1:
                    Sprite_obj.phase += 1
                    self.position_phase_actualisation(Sprite_obj)
                    self.FCT_phase_actualisation(Sprite_obj)

    def position_phase_actualisation(self, sprite):

        FCTposX = self._dict_["patern"][self.patern]["position"][str(sprite.phase)][str(sprite.position)]["x"]
        FCTposY = self._dict_["patern"][self.patern]["position"][str(sprite.phase)][str(sprite.position)]["y"]
        sprite.init_pos(FCTposX, FCTposY)

    def FCT_phase_actualisation(self, sprite):

        FCTnewPosX = self._dict_["patern"][self.patern]["fonction"][str(sprite.phase)][str(sprite.position)]["y"]
        FCTnewPosY = self._dict_["patern"][self.patern]["fonction"][str(sprite.phase)][str(sprite.position)]["y"]

        sprite.FCTnewposXX = FCTnewPosX
        sprite.FCTnewposYY = FCTnewPosY

    def startGame(self):
        if self.first_press_key:
            self.begin = pygame.time.get_ticks()
            self.first_press_key = None
            

    def update(self):
        
        if self.end_patern:
            self.Pause = True
            self.patern_choose()

        if self.begin != None:
            now = pygame.time.get_ticks()

            if not self.Pause and not self.end_patern and (now - self.begin) >= self.start:

                if now - self.last_ennemy_spawn >= self.Cooldown_ennemy and self.numbers_ennemy >= 2:
                    self.ennemy_init()

                self.__GroupBullet_Ennemy.update()
                self.__GroupSHIP.update()
                self.phase_statement()

    def draw(self, window):
          
        self.__GroupBullet_Ennemy.draw(window)
        self.__GroupSHIP.draw(window)