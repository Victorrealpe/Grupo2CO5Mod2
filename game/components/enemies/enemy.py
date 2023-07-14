import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH, ICE_TYPE


class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    SPEED_Y = 1
    SPEED_X = 3
    MOV_X = {0: 'left', 1: 'right'}
    IMAGE = {1: ENEMY_1, 2: ENEMY_2}
    

    def __init__(self, image = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = [30, 100]):
        self.image = self.IMAGE[image]
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = self.Y_POS
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30, 50)
        self.bullets = []
        self.shoot_num = 0
        self.control_dis = True
     

    def update(self, ships, game):

        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        
        self.change_movement_x()

        bullet = self.shoot(game.bullet_manager)
        if bullet is not None and self.control_dis == True:
            game.bullet_manager.add_bullet(bullet)

        if self.control_dis == False:
            game.bullet_manager.enemy_bullets = []

        #LOGICA DE BAJAR VIDA AL LLEGAR AL FINAL

        if self.rect.y >= SCREEN_HEIGHT:
            

            ships.remove(self)
            for heart in game.player.hearts:
                hearts_list = list(game.player.hearts)
                last_heart = hearts_list[-1] 
                if heart == last_heart:
                    game.player.hearts.remove(heart)
                    break


        vidas_disponibles = len(game.player.hearts) + 1
        if vidas_disponibles <= 1:
                game.death_count += 1
                game.playing = False
                pygame.time.delay(200)
                
                

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <=10):
            self.movement_x = 'right'
            self.index = 0

    def stop_movement(self):
        self.speed_y = 0
        self.speed_x = 0
        self.rect.y = self.rect.y
        self.rect.x = self.rect.x

    def stop_shoot(self):
        self.control_dis = False

    def ready_shoot(self):
        self.control_dis = True

    def ready_movement(self):
        self.speed_y = 1
        self.speed_x = 3


    
    def shoot(self, bullet_Manager):
        current_time = pygame.time.get_ticks()
        round_time = round((self.shooting_time - pygame.time.get_ticks())/1000)
        if round_time <= 0:
            bullet = Bullet(self)
            bullet_Manager.add_bullet(bullet)
            self.shoot_num += 1
            self.shooting_time = pygame.time.get_ticks()+2000





