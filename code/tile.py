import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __int__(self,position,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)