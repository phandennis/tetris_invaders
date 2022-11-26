import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x , y, projectile_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = projectile_image
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.projectile_speed = -11

    def update(self):
        """
         Sets the speed for the projectile and destroys the projectile if it is off-screen
        """
        self.rect.y += self.projectile_speed

        if self.rect.bottom < 0:
            self.kill()

