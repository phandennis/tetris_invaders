import pygame

class Mob(pygame.sprite.Sprite):
    """Mob Class to get the rect
    It has a set x and y for the position of the mob
    Speed will help indicate the counter speed
    Health was not implemented in the game
    Mob_Image so it gets the image of the mob 
    Args:
        pygame (_type_): _description_
    """
    def __init__(self, x, y, speed, health, mob_image):
        """Initalize the stats and position

        Args:
            x (int): X position
            y (int):  Y position
            speed (int): Utilize for how fast the mob goes down in the counter logic in update()
            health (int): Not implemented by wanted to make it so it requries multiple projectiles to hit and reduce the mobs hp
            mob_image (image): load the image with a variable and use pygame.image.load()
        """
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
        """Everytime the update is called, the counter goes up by 20
        When the counter divides 20 and it equals 0, the y position moves by the number of the speed of the mob
        When counter is 0, it shifts side by side by 10 on the x-axis
        If the counter is somehow 3000, it resets to 0
        """
        if self.counter % 20 == 0:
            self.rect.y += self.mob_speed
        if self.counter == 0:
            self.rect.x += 10
        if self.counter == 2000:
            self.rect.x -= 10
        self.counter += 20
        if self.counter == 3000:
            self.counter = 0

    
