import pygame
from base_game.screens import BaseScreen
from pygame import mixer

class Welcome(BaseScreen):
    # *args non-key worded, variable length argument list
    # **kwargs keyword arguments
    """Welcome screen for the game with a title, start and quit 

    Args:
        BaseScreen (Class): Base window class for all windows in the game to inherit
    """    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        mixer.init()
        pygame.mixer.music.load("./sound/background_music.ogg")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)



    def draw(self):
        """This overrides the draw method from the BaseScreen class"""

        background = pygame.image.load("./images/background.png")
        background_rect = background.get_rect(topleft=(0,0))
        self.window.blit(background, background_rect)

        title = pygame.image.load("./images/title.png").convert_alpha()
        title_rect = title.get_rect(center=(640,180))
        self.window.blit(title, title_rect)

        #press start button
        start = pygame.image.load("./images/start.png").convert_alpha()
        start_rect = start.get_rect(center=(640,380))
        self.window.blit(start, start_rect)

        if start_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.next_screen = "username"
                self.running = False

        #quit button
        quit = pygame.image.load("./images/quit.png").convert_alpha()
        quit_rect = quit.get_rect(center=(640,480))
        self.window.blit(quit, quit_rect)

        # When the mouse collides with the get_rect of the quit_rect, it will works
        if quit_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.next_screen = False
                self.running = False

    def update(self):
        pass
    
    def manage_event(self, event):
        """Tracks events

        Args:
            event : Event is recorded based on what the user inputs

        When they press space it starts the game by moving to the game screen "game.py"
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "username"
            self.running = False
        
