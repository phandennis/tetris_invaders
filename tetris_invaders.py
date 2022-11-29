import pygame
from screens import Welcome, GameScreen, GameOver


class Game(GameScreen):
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((1280, 720))

        pygame.display.set_caption("Tetris Shooter")

        pygame.font.init()

    def run(self):
        """Main method, manages interaction between screens"""
        self.all_sprites = pygame.sprite.Group()
        self.score = 0
        self.username = ''
        state = {}
        # These are the available screens
        screens = {
            "welcome": Welcome,
            "game": GameScreen,
            "game_over": GameOver
        }
        # Start the loop
        running = True
        current_screen = "welcome"
        while running:
            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")
            
            GameScreen.draw(self)
            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window, state)
            # Run the screen
            screen.run()
            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen
            state = screen.state


if __name__ == "__main__":
    tetris_shooter = Game()
    tetris_shooter.run()
