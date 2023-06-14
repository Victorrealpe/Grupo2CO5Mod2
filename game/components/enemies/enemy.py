import random
import pygame 
from pygame.sprite import _Group, Sprite
from Grupo2CO5Mod2.game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from game.utils.constants import ENEMY_1
from random import randint


class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    Y_POS = 20
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550]
    SPEED_Y = 1
    SPEED_X = 5
    MOV_X = {0: 'left', 1: 'right'}

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.X_POS_LIST[random.randint(0,10)]
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(30,100)
        self.index = 0

    def update(self, ships):
        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x

        else:
            self.rect.x += self.speed_x

        self.change_movement_x()

        #agregar validacion


        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)


    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))


    def change_movement_x(self):
        self.index += 1
        if(self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0

        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0

    # agregar manager de enemigos

                                                                        

