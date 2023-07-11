import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH, BG_MENU
from game.components.button import Button
import pygame, sys



class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2 - 70
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2 

    def __init__(self, messages, screen):
        screen.blit(BG_MENU, (0,0))
        self.screen = screen.blit(BG_MENU, (0,0))
        self.font = pygame.font.Font(FONT_STYLE, 50)

        self.text = self.font.render(messages[0], True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT *2)

        self.text1 = self.font.render(messages[1], True, (0,0,0))
        self.text_rect1 = self.text.get_rect()
        self.text_rect1.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT *2 + 60)

        self.text2 = self.font.render(messages[2], True, (0,0,0))
        self.text_rect2 = self.text.get_rect()
        self.text_rect2.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT *2 + 300)



        self.menu_back = False 

    def get_font(size): 
        return pygame.font.Font(FONT_STYLE, size)

    def update(self, game):
        pygame.display.update()
        #self.handle_events_on_menu(game)
        Menu.main_menu(self, self.screen,game)

    def draw (self, screen ):
        #screen.blit(self.text, self.text_rect,self.text1, self.text_rect1,self.text2, self.text_rect2)

        screen.blit(self.text, self.text_rect)
        screen.blit(self.text1, self.text_rect1)
        screen.blit(self.text2, self.text_rect2)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()



    def reset_screen_color(self, screen):
        screen.blit(BG_MENU,(0,0))
     


    def update_message(self, messages, screen, game):

        boton_grande0 = pygame.image.load("game/assets/Play Rect.png")
        boton_grande = pygame.transform.scale(boton_grande0, (500, 110))
     

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        self.text = self.font.render(messages[0], True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH - 10, SCREEN_HEIGHT/3 + 30)

        self.text1 = self.font.render(messages[1], True, (0,0,0))
        self.text_rect1 = self.text.get_rect()
        self.text_rect1.center = (self.HALF_SCREEN_WIDTH - 10, SCREEN_HEIGHT/3 + 100)

        self.text2 = self.font.render(messages[2], True, (0,0,0))
        self.text_rect2 = self.text.get_rect()
        self.text_rect2.center = (self.HALF_SCREEN_WIDTH - 70, SCREEN_HEIGHT/3 + 170)


        PLAY_BUTTON = Button(image=boton_grande, pos=(300, 500), 
            text_input="PLAY AGAIN", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        QUIT_BUTTON = Button(image=pygame.image.load("game/assets/Quit Rect.png"), pos=(850, 500), 
            text_input="EXIT", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game.run()
                    self.menu_back = False
             
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    self.menu_back = True
                    Menu.main_menu(self, screen, game)
            


    def main_menu(self, screen,game):



        global menu_volver 

        while game.death_count <= 0 or self.menu_back == True:
            #boton_grande0 = pygame.image.load("game/assets/Menu/Play Rect.png")
            #boton_grande = pygame.transform.scale(boton_grande0, (300, 100))
            
            screen.blit(BG_MENU,(0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = Menu.get_font(100).render("ATTACK IN SPACE", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(550, 80))

            PLAY_BUTTON = Button(image=pygame.image.load("game/assets/Play Rect.png"), pos=(550, 230), 
                                text_input="PLAY", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("game/assets/Options Rect.png"), pos=(550, 380), 
                                text_input="OPTIONS", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("game/assets/Quit Rect.png"), pos=(550, 530), 
                                text_input="QUIT", font=Menu.get_font(75), base_color="#d7fcd4", hovering_color="White")

            screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        game.run()
                        self.menu_back = False 
                        
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        #options()
                        pass
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        game.playing = False
                        game.running = False
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    

        

    