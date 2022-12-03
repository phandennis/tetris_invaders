from base_game.screens import BaseScreen
import pygame

class Username(BaseScreen):
    """Enter the username for the game to register into the json file"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state["name"] = ""

    def draw(self):
        print(pygame.time.get_ticks())

        background = pygame.image.load("./images/background.png")
        background_rect = background.get_rect(topleft=(0,0))
        self.window.blit(background, background_rect)

        # input self.username
        self.font = pygame.font.Font('./font/pixel2.ttf', 35)
        purple = (255, 0, 255)
        text_surface = self.font.render(f'Enter your username {self.state["name"]}', True, purple)
        input_rect = text_surface.get_rect(center=(640,310))
        self.window.blit(text_surface, (input_rect.x+5, input_rect.y))
        input_rect.w = max(100, text_surface.get_width()+10)

    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.next_screen = "game"
                self.running = False
            elif event.key == pygame.K_BACKSPACE:
                self.state["name"] = self.state["name"][:-1]
            else:
                self.state["name"] += str(event.unicode)

    def update(self):
        pass