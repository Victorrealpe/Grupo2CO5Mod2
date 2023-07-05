import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

#PODERES

CORAZON_scale = pygame.image.load(os.path.join(IMG_DIR, 'Other/CORAZON.png'))
CORAZON = pygame.transform.scale(CORAZON_scale, (70, 90))

BOMB_scale = pygame.image.load(os.path.join(IMG_DIR, 'Other/BOMB.png'))
BOMB = pygame.transform.scale(BOMB_scale, (60, 70))





DEFAULT_TYPE = "default"
HEART_TYPE = "heart"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'
BOMB_TYPE = 'bomb'


SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

#MENU
BG_MENU0 = pygame.image.load(os.path.join(IMG_DIR, 'Other/FONDO_MENU.jpg'))
BG_MENU =  pygame.transform.scale(BG_MENU0, (1200, 800))

# SOUNDS

#SONIDO DEL JUEGO
SOUND_BASE = os.path.join(IMG_DIR, "Sound/SONIDO_BASE.mp3")

#DISPAROS
SOUND_BULLET_PLAYER = os.path.join(IMG_DIR, "Sound/DISPAROS_PLAYER.mp3")
SOUND_BULLET_ENEMY = os.path.join(IMG_DIR, "Sound/DISPAROS_ENEMY.mp3")

#MUERTE
SOUND_MUERTE = os.path.join(IMG_DIR, "Sound/SONIDO_MUERTE.wav")

#ANIMACION DE EXPLOCION

EXPLOSION_1 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/1.png"))
EXPLOSION_2 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/2.png"))
EXPLOSION_3 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/3.png"))
EXPLOSION_4 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/4.png"))
EXPLOSION_5 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/5.png"))
EXPLOSION_6 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/6.png"))
EXPLOSION_7 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/7.png"))
EXPLOSION_8 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/8.png"))
EXPLOSION_9 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/9.png"))
EXPLOSION_10 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/10.png"))
EXPLOSION_11 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/10.png"))
EXPLOSION_12 = pygame.image.load(os.path.join(IMG_DIR, "Explosion/10.png"))



FONT_STYLE = 'freesansbold.ttf'
