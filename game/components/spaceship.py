
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP
class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'

    def update(self, game, user_input ):
        self.shoot(game.bullet_manager, user_input)


        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()

        # Verificar si la nave cruzó el límite en el eje X
        if self.rect.left <= 0:
            self.rect.right = SCREEN_WIDTH  # Colocar la nave al lado contrario
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.left = 0
        elif user_input[pygame.K_UP]:
            if self.rect.y > 0:
                self.move_up()
        elif user_input[pygame.K_DOWN]:
            if self.rect.y < 540:
                self.move_down()

        

        

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.right >= SCREEN_WIDTH - self.SHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y +=  self.SHIP_SPEED   

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager,user_input):
        if user_input[pygame.K_SPACE]:
            bullet = Bullet(self, 'player')
            bullet_manager.add_bullet(bullet)