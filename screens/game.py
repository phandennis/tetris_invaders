import pygame
from base_game.screens import BaseScreen
from sprites import Mob, Player, Projectile
from pygame import mixer
import json

ship = pygame.image.load('./images/player.png')
p_ = Player(ship)
p_.rect.centerx = 640
p_.rect.bottom = 700



class GameScreen(BaseScreen, Player, Mob, Projectile):
    # *args non-key worded, variable length argument list
    # **kwargs keyword arguments
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        BLACK = (0,0,0)
        self.window.fill(BLACK)
        self.all_sprites = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.projectile = pygame.sprite.Group()
        self.player1 = pygame.sprite.GroupSingle()
        self.player1.add(p_)
        time = pygame.time.Clock()
        time.tick(60)
        self.username = 'Bob'
    

        

        mixer.init()
        pygame.mixer.music.load("./sound/game.ogg")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(loops=-1)


        # images of mobs
        self.mob_J = pygame.image.load('./images/j_mob.png')
        self.mob_L = pygame.image.load('./images/L_mob.png')
        self.mob_I = pygame.image.load('./images/I_mob.png')
        self.mob_O = pygame.image.load('./images/o_mob.png')

        # projectile image
        self.projectile_image = pygame.image.load('./images/laser_projectile.png')

        self.score = 0

        self.high_score = 0

    def create_tetris_blocks(self, width, height, offsetx, offsety, distdiff, mob_info):
        speed = mob_info[0]
        health = mob_info[1]
        mob_img = mob_info[2]
        for x in range(width):
            for y in range(height):
                m = Mob(offsetx + x * distdiff, offsety + y * distdiff, speed, health, mob_img)
                self.mobs.add(m)
                self.all_sprites.add(m)


    def draw(self):
        """This overrides the draw method from the BaseScreen class"""
        background = pygame.image.load("./images/game_background.png")
        background_rect = background.get_rect(topleft=(0,0))
        self.window.blit(background, background_rect)

        
        purple = (186,85,255)
        self.font = pygame.font.Font('./font/pixel2.ttf', 35)
        scoreboard = self.font.render(f'Score {self.score}', True, purple)
        scoreRect = scoreboard.get_rect(center=(150, 650))
        self.window.blit(scoreboard, scoreRect)

        self.all_sprites.add(p_)

        # draw all sprites
        self.all_sprites.draw(self.window)




    def manage_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                projectile = Projectile(p_.rect.centerx, p_.rect.top, self.projectile_image)
                self.all_sprites.add(projectile)
                self.projectile.add(projectile)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("./sound/shooting.wav"), maxtime=600)
        

    def update(self):

        # updates all the sprites
        self.all_sprites.update()
        self.J_mob = (1, 2, self.mob_J)
        self.L_mob = (1, 4, self.mob_L)
        self.I_mob = (1, 2, self.mob_I)
        self.O_mob = (1, 4, self.mob_O)

        # spawns the mobs
        if len(self.mobs) == 0:
            self.create_tetris_blocks(4, 5, 405, 0, 50, self.J_mob)
            self.create_tetris_blocks(1, 1, 315, 20, 0, self.L_mob)
            self.create_tetris_blocks(1, 12, 610, 10, 0, self.O_mob)
            self.create_tetris_blocks(1, 12, 210, 10, 0, self.I_mob)
        
        current_time = pygame.time.get_ticks()
        if (8999 < current_time < 9001):
           self.create_tetris_blocks(5, 4, 300, 0, 50, self.I_mob)
        
        if (5998 < current_time < 6001):
            self.create_tetris_blocks(4, 3, 610, 0, 50, self.O_mob)


        for projectile in self.projectile:
            if pygame.sprite.spritecollide(projectile, self.mobs, 1):
                self.score = self.score + 50        

        for player in self.player1:
            if pygame.sprite.spritecollide(player, self.mobs, 1):
                self.score = self.score - 50

        l = []
        for mob in self.mobs:
            if mob.rect.bottom == 720:
                with open("./data/scores.json", "w", 'utf-8') as f:
                    new_score = {
                        'username': {self.username},
                        'score': {(self.score)}
                        }
                    l.append(new_score)
                    json.dump(l, f)

                self.next_screen = "game_over"
                self.running = False

        




                    





        
        
        


        