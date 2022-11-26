from os import stat_result
import pygame
import random
import time
import os.path
from .mob import Mob

class Player(pygame.sprite.Sprite):

    def __init__(self, player_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()

        

    def update(self):
        """
        Player's ability to move left or right and restricted from moving out of the screen
        """
        self.movement = 0
    # moves the player left or right
        keystroke = pygame.key.get_pressed()
        if keystroke[pygame.K_LEFT]:
            self.movement += -1
        if keystroke[pygame.K_RIGHT]:
            self.movement += +1
        self.rect.x += self.movement
        self.rect.centerx += self.movement

    # makes sure player cannot get off screen
        if self.rect.right > 1280:
            self.rect.right = 1280
        if self.rect.left < 0:
            self.rect.left = 0


