import pygame

class Mob(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, health, mob_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_image
        self.stats = (speed, health)
        if self.stats == (1, 2):
            self.points = 100
        if self.stats == (1, 4):
            self.points = 200
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.mob_speed = speed
        self.counter = 0
        self.mob_health = health

    def update(self):
        if self.counter % 20 == 0:
            self.rect.y += self.mob_speed
        if self.counter == 0:
            self.rect.x += 10
        if self.counter == 2000:
            self.rect.x -= 10
        self.counter += 20
        if self.counter == 3000:
            self.counter = 0

    