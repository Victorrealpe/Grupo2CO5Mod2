
import pygame
from game.utils.constants import HEART
from pygame.sprite import Sprite


class Heart(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = HEART
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y