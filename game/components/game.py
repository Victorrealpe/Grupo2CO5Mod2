import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.power_ups.power_up_manager import PowerUpManager
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SOUND_BASE, HEART_TYPE
from game.components.spaceship import Spaceship
from game.components.heart import Heart 

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.death_count = 0
        self.score = 0
        self.high_score = 0
        self.menu = Menu ('SPACE ATTACK', self.screen)

    
    def execute (self):
        sound_game= pygame.mixer.Sound(SOUND_BASE)
        sound_game.set_volume(0.1) #CONTROL DE VOLUMEN
        pygame.mixer.Sound.play(sound_game)
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score = 0
        self.bullet_manager.reset() 
        self.enemy_manager.reset() 
        self.playing = True
        self.player.add_vida()
        
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
       
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)

        for enemy in self.enemy_manager.enemies:
            enemy.update(self.enemy_manager.enemies, self)

        self.enemy_manager.update(self)
        self.bullet_manager.update(self, self.player)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.player.hearts.draw(self.screen)
        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
            
        self.y_pos_bg += self.game_speed











    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT //2

        self.menu.reset_screen_color(self.screen)
        self.menu.main_menu(self.screen,self)

        if self.death_count >0:
            self.menu.update_message(f'Score: {str(self.score)}    '+ f'Death: {str(self.death_count)}    ' + f'High Score: {str(self.high_score)}')
        icon = pygame.transform.scale (ICON, (80,120))
        self.screen.blit(icon, (half_screen_width - 50, half_screen_height -150))

        self.menu.draw(self.screen)
        self.menu.update(self)











        
    def update_score(self):
        self.score += 1

    def update_reset_power(self):
        self.agregar_vida = False

    
    
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (100, 100)
        self.screen.blit(text, text_rect)

        if self.score > self.high_score:
            self.high_score = self.score
        
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)

            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 30)
                text = font.render(f'{str(self.player.power_up_type).capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                text_rect = text.get_rect()
                self.screen.blit(text,(540, 50))
            else:
                self.player_has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

        if self.player.has_power_up and self.player.power_up_type == HEART_TYPE:
            total_vidas = len(self.player.hearts)
            max_vidas = 10
            if total_vidas < max_vidas:
                self.player.vidas += 1
                x = 40 + self.player.vidas * 40
                y = 20
                heart_mas = Heart(x, y)
                self.player.hearts.add(heart_mas) 
                self.player.has_power_up = False

                
        

            




