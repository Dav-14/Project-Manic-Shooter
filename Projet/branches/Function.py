import os
import time

import pygame
from pygame.locals import *

import Entity.Hero as mHero
import Entity.Ennemis as mEnnemis

def __Draw():
    Window.blit(Background, (0,0))
    Window.blit(Spaceship.style, (Spaceship.posX, Spaceship.posY))
