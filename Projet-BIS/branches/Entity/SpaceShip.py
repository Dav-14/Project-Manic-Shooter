import time
import os
import pygame
from pygame.locals import * 
import Entity.Reactor as Rct

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, typ, style, __speed__,bullet_type):#Il y a 2 type SpaceShip et Ennemy, ils nous aideront pour les insteractions entre group
        super().__init__()
        Surface = pygame.display.get_surface()#Recupere la surface de la fenetre
        self.Surf_Width, self.Surf_Height = Surface.get_width(), Surface.get_height()#Recupere sa longeur et largeur
        self.area = Surface.get_rect()
        ####################################
        self.type = typ
        ### CHARGEMENT DU STYLE VAISSEAU ###
        self.style = self.type + "_" + str(style)
        #fullpath = os.path.join("..", "Ressources", "Graphics", self.type, style)
        self.image = pygame.image.load(os.path.join("..", "Ressources", "Graphics", self.type, self.style + ".png")).convert_alpha()#Charge l'image
        coef = (self.image.get_height())/(self.image.get_width())#Calcul le coef de proportion de l'objet
        self.width = 40#On les tailles de la résolution de l'image
        #Mettre un fichier Json pour répertorié les tailles en fonction des images. 
        self.height = int(coef * self.width)
        self.image = pygame.transform.scale(self.image, (self.width,self.height))#Puis on appliques les nouvelles proportion
        self.rect = self.image.get_rect()
        ####################################
        ## INFO POUR LA CLASSE BULLET
        self.bullet_type = bullet_type
        self.bullet_last_hit = pygame.time.get_ticks()
        
        #INFO VAISSEAU
        self.__speed__ = __speed__
        #self.life

        self.posX = self.rect.x = self.Surf_Width/2 - self.width/2
        self.posY = self.rect.y = self.Surf_Height*(1-(5/80)) - self.height
        
        self.Reactor = None

    def Reactor_innit(self):
        if self.Reactor == None:
            pass
            #self.Reactor = Rct.reactor_f(self)

    def shoot(self):#Faire avec un fichier Json qui définira en fonction du type le tire qui sera en direction du HAUT ou du BAS, ou encore change la fonction du TIR,
        #Plus simple faire un fichier de patern de tire qui bougera un élément en fonction de sa position, conclusion vers le haut fonction négative, vers le bas -> fonction positive.
        pass

