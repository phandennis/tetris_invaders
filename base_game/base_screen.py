import pygame
from pygame import mixer

class BaseScreen:
    """
    Base class for the game screens
    """

    def __init__(self, window):
        # surface for the window
        self.window = window


        # default, when True it can switch to another screen
        self.next_screen = False

    def run(self):
        """
        This is the main method for the class.
        This manages the event loop, and:
        sets the game at 60 FPS,
        calls `update` and `draw`
        calls `manage_event` for each event recieved
        quits the game if the quit button is pressed on or escape key is pressed
        """

        #fps = pygame.time.Clock()
        self.running = True
        while self.running:
            #fps.tick(144)
            self.update()
            self.draw()
            pygame.display.update()

            for event in pygame.event.get():
                self.manage_event(event)
                # To exit the game
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False
                #call the manage_event method

#everything has a hitbox of a rectangle
    @property
    def rect(self):
        return self.window.get_rect()

    def draw(self):
        print("You should override the DRAW method in your class")
    
    def update(self):
        print("You should override the UPDATE method in your class")
    
    def manage_event(self, event):
        print("You should override the manage_event method in your class")