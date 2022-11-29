import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x , y, projectile_image):
        """This is the projectile that the player shoots out in the space invader-like game

        Args:
            x (int): This sets the x position which was used to attach to the player position at the centerx 
            y (int): It is used to attach to the player image on top
            projectile_image (image): loads an image with pygame.image.load()
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = projectile_image
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.projectile_speed = -11

    def update(self):
        """
         Sets the speed for the projectile and destroys the projectile if it is off-screen (when it reachs the top)
        """
        self.rect.y += self.projectile_speed

        if self.rect.bottom < 0:
            self.kill()

