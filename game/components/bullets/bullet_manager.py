import pygame
from game.utils.constants import EXPLOSION_1, EXPLOSION_10, EXPLOSION_11, EXPLOSION_12, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9
from game.utils.constants import SHIELD_TYPE, SOUND_MUERTE, HEART_TYPE



class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []


    def update (self, game, spaceship):

   


        for bullet in self.bullets:
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    sound_muerte = pygame.mixer.Sound(SOUND_MUERTE)
                    pygame.mixer.Sound.play(sound_muerte)
                    game.score += 100
                    self.explosion(game,enemy)
                    game.enemy_manager.enemies.remove((enemy))
                    
                    self.bullets.remove(bullet)
                    for bullet in self.enemy_bullets:
                        self.enemy_bullets.remove(bullet)

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy': 
                sound_muerte = pygame.mixer.Sound(SOUND_MUERTE)
                #sound_muerte1.set_volume(1) #CONTROL DE VOLUMEN
                sound_muerte.play()
                if game.player.power_up_type != SHIELD_TYPE:
                    hearts_list = list(spaceship.hearts)
                    vidas_disponibles = len(hearts_list)
                    last_heart = hearts_list[-1] 
                    hearts_list.remove(last_heart)
                    spaceship.vidas -= 1
                    spaceship.hearts = pygame.sprite.Group(hearts_list)
                    
                    if vidas_disponibles == 1:
                        game.death_count += 1
                        game.playing = False
                        pygame.time.delay(200)
                        break
                if game.player.power_up_type == HEART_TYPE:
                    for Heart in spaceship.hearts:
                        spaceship.hearts.add(Heart)
                        break

                self.enemy_bullets.remove(bullet)

        for bullet in self.bullets:
            bullet.update(self.bullets)  # Actualizar posición de balas del jugador

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)  # Actualizar posición de balas enemigas

    
    def draw (self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def explosion(self, game, enemigo):
        x = enemigo.rect.x + (enemigo.rect.width - EXPLOSION_1.get_width()) // 2
        y = enemigo.rect.y + (enemigo.rect.height - EXPLOSION_1.get_height()) // 2

        imagenes_explosion = [EXPLOSION_1, EXPLOSION_2, EXPLOSION_3, EXPLOSION_4, EXPLOSION_5, EXPLOSION_6, EXPLOSION_7, EXPLOSION_8, EXPLOSION_9, EXPLOSION_10, EXPLOSION_11, EXPLOSION_12]

        for i, imagen_explosion in enumerate(imagenes_explosion):
            game.screen.blit(imagen_explosion, (x, y-10))

            pygame.display.flip()

    def add_bullet(self, bullet):


        if bullet.owner == "enemy":
                self.enemy_bullets.append(bullet)

        elif bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)

        elif bullet.owner == "enemy":
            self.enemy_bullets.append(bullet)


           
    
    def reset(self):
        self.bullets = []
        self.player_bullets = []
        self.enemy_bullets = []
