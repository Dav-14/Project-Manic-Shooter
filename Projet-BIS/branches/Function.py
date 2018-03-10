import os
import time

import pygame
from pygame.locals import *

def __Draw():
    Window.blit(Background, (0,0))
    Window.blit(Spaceship.style, (Spaceship.posX, Spaceship.posY))
