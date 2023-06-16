import pygame

from game.components.enemies.enemy_manager import EnemyManager


class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.enemy_manager = EnemyManager()  # Crear una instancia de EnemyManager

    def update (self, game):

        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    game.score += 100
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                game.death_count += 1
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break
        #se agrega funcion de suceso de la bala nave
        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in self.enemy_manager.enemies:  # Acceder a enemies desde la instancia de EnemyManager
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    self.bullets.remove(bullet)
                    self.enemy_manager.enemies.remove(enemy)
                    #agregar explocion


    def draw (self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
<<<<<<< HEAD
        if bullet.owner == 'enemy' and len (self.enemy_bullets)<1:
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'player':
            self.bullets.append(bullet)
=======
        if bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)
        elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
    
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []
>>>>>>> 6bbeb075f5d6d0a4e4250a051138bd57f9d0780d
