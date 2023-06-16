
import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT


class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET, (10,20))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY, (10,20))
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 20

    def __init__(self, spaceshift, direction):
        self.image = self.BULLETS[spaceshift.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceshift.rect.center
        self.owner = spaceshift.type
        self.direction = direction #parametro para saber la direccion del disparo

    def update(self, bullets):
<<<<<<< HEAD
        #self.rect.y += self.SPEED #viejo codigo
        if self.direction == 'player':
            self.rect.y -= self.SPEED
        elif self.direction == 'enemy':
            self.rect.y += self.SPEED

        if self.rect.y>= SCREEN_HEIGHT or self.rect.y <= 0: #se agrega que si la bala va para arriba se borra tambien 
=======

        if self.owner == 'player':
            self.rect.y -= self.SPEED
        else:
            self.rect.y += self.SPEED

        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
>>>>>>> 6bbeb075f5d6d0a4e4250a051138bd57f9d0780d
            bullets.remove(self)




    def draw(self, screen):
        screen.blit(self.image, self.rect)

