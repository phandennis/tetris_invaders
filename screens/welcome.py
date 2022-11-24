import pygame
from base_game.screens import BaseScreen

class Welcome(BaseScreen):
    # *args non-key worded, variable length argument list
    # **kwargs keyword arguments
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen = pygame.display.set_mode((1280,720))



    def draw(self):
        """This overrides the draw method from the BaseScreen class"""

        background = pygame.image.load("./assets/background.png")
        background_rect = background.get_rect(topleft=(0,0))
        self.window.blit(background, background_rect)

        title = pygame.image.load("./assets/title.png")
        title_rect = title.get_rect(center=(640,200))
        self.window.blit(title, title_rect)

        #press start button
        start = pygame.image.load("./assets/start.png")
        start_rect = start.get_rect(center=(640,350))
        self.window.blit(start, start_rect)

        if start_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.next_screen = "game"
                self.running = False


        #pygame.display.update()


    def update(self):
        pass
    
    def manage_event(self, event):
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
        