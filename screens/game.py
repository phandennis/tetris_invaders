import pygame
from base_game.screens import BaseScreen
from sprites import Mob, Player, Projectile
from pygame import mixer
import json
from datetime import datetime

# loads the player which is a ship from the Class Player
ship = pygame.image.load('./images/player.png')
p_ = Player(ship)

# sets the spawn point for the player
p_.rect.centerx = 640
p_.rect.bottom = 700

# time for the game
fps = pygame.time.Clock()

class GameScreen(BaseScreen, Player, Mob, Projectile):
    """Initiate the game which includes the Player, Mob and Projectile classes
    All of these classes are sprites in the game.

    Args:
        BaseScreen (Class): This is the base of all the screens in the game
        Player (Sprite): This is the ship in the game where you can move with the arrow keys
        Mob (Sprite): This is the mobs aka the tetris blocks falling in the game
        Projectile (Sprite): This is the sprite that comes out of the ship/player which shoots and hits tetris blocks
    """
    # *args non-key worded, variable length argument list
    # **kwargs keyword arguments
    def __init__(self, *args, **kwargs):
        """Grabs all key and non keywords from inherited classes
        """
        super().__init__(*args, **kwargs)

        # groups all the sprites into one sprite group
        self.all_sprites = pygame.sprite.Group()

        # groups only the tetris blocks sprites
        self.mobs = pygame.sprite.Group()

        # groups only the projectiles sprites
        self.projectile = pygame.sprite.Group()

        # groups a single sprite only or none
        self.player1 = pygame.sprite.GroupSingle()
        self.player1.add(p_)

        # default setting for the username
        self.username = 'RandomUsername123'


        # initiates the music
        mixer.init()

        # background music for the GameScreen
        pygame.mixer.music.load("./sound/tetris_theme.ogg")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)


        # images of mobs
        self.mob_J = pygame.image.load('./images/j_mob.png')
        self.mob_L = pygame.image.load('./images/L_mob.png')
        self.mob_I = pygame.image.load('./images/I_mob.png')
        self.mob_O = pygame.image.load('./images/o_mob.png')
        self.mob_S = pygame.image.load('./images/S_mob.png')
        self.mob_T = pygame.image.load('./images/T_mob.png')
        self.mob_Z = pygame.image.load('./images/Z_mob.png')

        # projectile image
        self.projectile_image = pygame.image.load('./images/laser_projectile.png')

        # sets the default score
        self.score = 0

    def create_tetris_blocks(self, row, column, offsetx, offsety, distdiff, mob_info):
        """Creates tetris blocks aka the mobs and adds them to the sprite groups
        such as self.mobs and self.all_sprites

        Args:
            width (int): This sets how many mobs in a row
            height (int): This sets how many mobs in a column
            offsetx (int): This sets where they spawn on the x-axis
            offsety (int): This sets where they spawn on the y-axis
            distdiff (int): Distance between each mob when they spawn and how much the shift as the counter goes on in Mob Class
            mob_info (load an image with pygame): This is just the image of the mob 
        """
        speed = mob_info[0]
        health = mob_info[1]
        mob_img = mob_info[2]
        for x in range(row):
            for y in range(column):
                m = Mob(offsetx + x * distdiff, offsety + y * distdiff, speed, health, mob_img)
                self.mobs.add(m)
                self.all_sprites.add(m)

    def pause(self):
        # pause image
        paused1 = pygame.image.load("./images/paused.png")
        paused1_rect = paused1.get_rect(center=(640,200))
        self.window.blit(paused1, paused1_rect)


    def draw(self):
        """This overrides the draw method from the BaseScreen class
        This method:
        draws the background,
        draws the scoreboard,
        draws all sprites,
        draws username entry,
        draws the seven wave images and plays the corresponding sound at a certain time in the game
        When the game is over, it records the username input and the score and the date
        """

        # draws and blit the background image from image directry
        background = pygame.image.load("./images/game_background.png")
        background_rect = background.get_rect(topleft=(0,0))
        self.window.blit(background, background_rect)

        # sets the colour purple
        purple = (186,85,255)

        # this is the text for score on the screen
        self.font = pygame.font.Font('./font/pixel2.ttf', 35)
        scoreboard = self.font.render(f'Score {self.score}', True, purple)
        scoreRect = scoreboard.get_rect(center=(150, 650))
        self.window.blit(scoreboard, scoreRect)

        # adds the plauer the all_sprites Group
        self.all_sprites.add(p_)

        # draw all sprites
        self.all_sprites.draw(self.window)


        # input self.username
        text_surface = self.font.render(f'Enter your username {self.username}', True, purple)
        input_rect = text_surface.get_rect(center=(900,650))
        self.window.blit(text_surface, (input_rect.x+5, input_rect.y))
        input_rect.w = max(100, text_surface.get_width()+10)

        # wave 1 image
        wave1 = pygame.image.load("./images/wave1.png")
        wave1_rect = wave1.get_rect(center=(640,300))

        # wave 2 image
        wave2 = pygame.image.load("./images/wave2.png")
        wave2_rect = wave2.get_rect(center=(640,300))

        # wave 3 image
        wave3 = pygame.image.load("./images/wave3.png")
        wave3_rect = wave3.get_rect(center=(640,300))

        # wave 4 image
        wave4 = pygame.image.load("./images/wave4.png")
        wave4_rect = wave4.get_rect(center=(640,300))

        # wave 5 image
        wave5 = pygame.image.load("./images/wave5.png")
        wave5_rect = wave5.get_rect(center=(640,300))

        # wave 6 image
        wave6 = pygame.image.load("./images/wave6.png")
        wave6_rect = wave6.get_rect(center=(640,300))

        # wave 7 image
        wave7 = pygame.image.load("./images/wave7.png")
        wave7_rect = wave7.get_rect(center=(640,300))

        current_time = pygame.time.get_ticks()


        # wave 1
        if (2310 < current_time < 3636):
            self.window.blit(wave1, wave1_rect)

        if (2210 < current_time < 2536):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./sound/wave1.ogg"))
            pygame.mixer.Channel(2).set_volume(2.0)

        # wave 2
        if (12210 < current_time < 14636):
            self.window.blit(wave2, wave2_rect)

        if (12210 < current_time < 12936):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./sound/wave2.ogg"))
            pygame.mixer.Channel(2).set_volume(2.0)

        # wave 3
        if (20310 < current_time < 24636):
            self.window.blit(wave3, wave3_rect)

        if (20210 < current_time < 20936):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./sound/wave3.ogg"))
            pygame.mixer.Channel(2).set_volume(2.0)

        # wave 4
        if (30310 < current_time < 34636):
            self.window.blit(wave4, wave4_rect)

        if (30210 < current_time < 30836):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./sound/wave4.ogg"))
            pygame.mixer.Channel(2).set_volume(2.0)

        # wave 5
        if (40310 < current_time < 42736):
            self.window.blit(wave5, wave5_rect)

        if (40210 < current_time < 40936):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./sound/wave5.ogg"))
            pygame.mixer.Channel(2).set_volume(2.0)

        # wave 6
        if (50310 < current_time <54636):
            self.window.blit(wave6, wave6_rect)

        if (50210 < current_time < 50936):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./sound/wave6.ogg"))
            pygame.mixer.Channel(2).set_volume(2.0)

        # wave 7
        if (67310 < current_time < 69636):
            self.window.blit(wave7, wave7_rect)

        if (67210 < current_time < 67936):
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./sound/wave7.ogg"))
            pygame.mixer.Channel(2).set_volume(2.0)

    def manage_event(self, event):
        """
        This tracks what the user can input:
        BACKSPACE will delete a character of the entry for username
        SPACE will shoot a projectile and if it hits something it makes a sound effect

        Args:
            event: This tracks the events
        """

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                self.username = self.username[:-1]
            elif event.key != pygame.K_SPACE:
                self.username = self.username + event.unicode


            if event.key == pygame.K_SPACE:
                projectile = Projectile(p_.rect.centerx, p_.rect.top, self.projectile_image)
                self.all_sprites.add(projectile)
                self.projectile.add(projectile)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("./sound/shooting.wav"), maxtime=600)
                pygame.mixer.Channel(0).set_volume(0.1)

    def update(self):
        """
        Updates the time with fps.tick()
        Updates all the sprites with the group all_sprites
        Sets the values for all the mobs 
        Spawns 7 waves based on time 
        Spawns mobs when there are no mobs and after 80 seconds
        When mobs hit the bottom of the screen, the game window turns to game over window
        When projectile hits, it kills itself and the sprite it collids
        """
        # updates all the sprites
        fps.tick()
        current_time = pygame.time.get_ticks()
        self.all_sprites.update()
        self.J_mob = (1, 1, self.mob_J)
        self.L_mob = (1, 1, self.mob_L)
        self.I_mob = (1, 2, self.mob_I)
        self.O_mob = (1, 4, self.mob_O)
        self.S_mob = (1, 4, self.mob_S)
        self.T_mob = (1, 2, self.mob_T)
        self.Z_mob = (1, 4, self.mob_Z)
        # spawns the mobs
        # J L O I S T Z


        # Spawn mobs based on time that starts only on the game screen
        ### WAVE 1 ###
        if (2309 < current_time < 2339):
            self.create_tetris_blocks(1, 1, 110, 0, 100, self.L_mob)
            self.create_tetris_blocks(1, 1, 310, 0, 100, self.L_mob)
            self.create_tetris_blocks(1, 1, 710, 0, 100, self.L_mob)
            self.create_tetris_blocks(1, 1, 410, 0, 100, self.L_mob)
            self.create_tetris_blocks(1, 1, 390, 0, 100, self.L_mob)
            self.create_tetris_blocks(1, 1, 910, 0, 100, self.L_mob)

        ### WAVE 2 ###
        if (13999 < current_time < 14025):
            self.create_tetris_blocks(2, 2, 300, 0, 50, self.J_mob)

        ### WAVE 3 ###
        if (22000 < current_time < 22029):
            self.create_tetris_blocks(3, 3, 300, 0, 50, self.O_mob)

        ### WAVE 4 ###
        if (30999 < current_time < 31025):
            self.create_tetris_blocks(4, 4, 300, 0, 50, self.I_mob)

        ### WAVE 5 ###
        if (40999 < current_time < 41025):
            self.create_tetris_blocks(5, 5, 300, 0, 50, self.S_mob)

        ### WAVE 6 ###
        # 50 seconds, milliseconds of 25, at this time it will spawn T mob in a 6 rows and 6 columns, at the x-axis of 300 and shifts 50 in the same area sideways
        if (51000 < current_time < 51025):
            self.create_tetris_blocks(6, 6, 300, 0, 50, self.T_mob)

        # After 70 seconds, between the milliseconds of 25 and 50, it will spawn the Z tetris blocks in 7 rows with 7 columns at the x axis of 600 and shifts 50
        # in the same spot
        ### WAVE 7 ###
        if (70025 < current_time < 70050):
            self.create_tetris_blocks(7, 7, 600, 0, 50, self.Z_mob)

        # when there are no mobs and the time is past 80 seconds, it will spawn these mobs
        if len(self.mobs) == 0 and current_time > 80000:
            self.create_tetris_blocks(1, 1, 110, 0, 50, self.T_mob)
            self.create_tetris_blocks(1, 1, 310, 0, 50, self.Z_mob)
            self.create_tetris_blocks(1, 1, 710, 0, 50, self.S_mob)
            self.create_tetris_blocks(1, 1, 410, 0, 50, self.J_mob)
            self.create_tetris_blocks(1, 1, 390, 0, 50, self.O_mob)
            self.create_tetris_blocks(1, 1, 910, 0, 50, self.I_mob)
            self.create_tetris_blocks(1, 1, 50, 0, 50, self.L_mob)


        # When a projectile hits a mob in the self.mob sprite group, it plays a sound and kills itself (the projectile)
        for projectile in self.projectile:
            if pygame.sprite.spritecollide(projectile, self.mobs, 1):
                self.score = self.score + 50
                projectile.kill()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("./sound/explosion1.wav"), maxtime=600) 
                pygame.mixer.Channel(1).set_volume(0.1) 

        # If a player collids with a mob then it will kill the mob and the score goes -50, and yes it can go negative
        for player in self.player1:
            if pygame.sprite.spritecollide(player, self.mobs, 1):
                self.score = self.score - 50

        # When any mob hits the bottom, it checks every sprite in the group sprite, the game will go to game over screen
        for mob in self.mobs:
            if mob.rect.bottom == 720:
                self.next_screen = "game_over"
                self.running = False

        # Records the username, score and date when the game is over to the json file in ./data/scores.json
        if self.next_screen == "game_over":
            entry = { "username": f'{self.username}', "score": int(f'{self.score}'), "date": datetime.today().strftime('%Y-%m-%d') }
            with open("./data/scores.json", "r") as file:
                data = json.load(file)
                data.append(entry)
                with open("./data/scores.json", "w") as f:
                    json.dump(list(data), f)


        




                    





        
        
        


        
