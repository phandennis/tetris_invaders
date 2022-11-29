import pygame
from base_game.screens import BaseScreen
from pygame import mixer

class GameOver(BaseScreen):
    # *args non-key worded, variable length argument list
    # **kwargs keyword arguments
    """The GameOver class 
    which has methods of 
    draw,
    update,
    manage_event

    Args:
        BaseScreen (Class): Base Screen for all the screens in the game
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = 0

        mixer.init()
        pygame.mixer.music.load("./sound/gameover.wav")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    def draw(self):
        """This overrides the draw method from the BaseScreen class
        
        It loads:
        background image
        game over text
        try again text
        quit text
        """

        background = pygame.image.load("./images/background.png")
        background_rect = background.get_rect(topleft=(0,0))
        self.window.blit(background, background_rect)

        gameover = pygame.image.load("./images/gameover.png").convert_alpha()
        go_rect = gameover.get_rect(center=(640,160))
        self.window.blit(gameover, go_rect)

        #press start button
        try_again = pygame.image.load("./images/tryagain.png").convert_alpha()
        try_rect = try_again.get_rect(center=(640,350))
        self.window.blit(try_again, try_rect)

        if try_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.next_screen = "game"
                self.running = False

        #quit button
        quit = pygame.image.load("./images/quit.png").convert_alpha()
        quit_rect = quit.get_rect(center=(640,450))
        self.window.blit(quit, quit_rect)

        if quit_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.next_screen = False
                self.running = False

    def update(self):
        pass
    
    def manage_event(self, event):
        pass
