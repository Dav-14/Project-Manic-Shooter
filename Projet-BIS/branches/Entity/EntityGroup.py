import time
import os
import pygame
from pygame.locals import *

class Entity(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)