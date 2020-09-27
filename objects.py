import pygame
from pygame.locals import *
import os
# from spritesheet import Spritesheet

ALPHA = (255,255,255)

class Player(pygame.sprite.Sprite):

    # Spawn player
    def __init__(self, spawnx, spawny, health, maxhealth, img, img_frames, ALPHA=ALPHA):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.maxhealth = maxhealth
        self.frame = 0              # count frames
        self.movex = 0              # move along x
        self.movey = 0              # move along y
        self.images = []
        self.is_jumping = False     
        self.is_falling = True
        self.fall_speed = 3.2

        for i in range(0,img_frames):
            image = pygame.image.load(os.path.join('assets/', f'{img}{i}.png')).convert()
            image.convert_alpha()
            image.set_colorkey(ALPHA)
            self.images.append(image)
        
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = spawnx
        self.rect.y = spawny

    # Control player movement
    def move(self, x, y):
        self.movex += x
        self.movey += y

    # Define player gravity
    def gravity(self, fall_speed=0):
        if fall_speed == 0:
            fall_speed = self.fall_speed

        if self.is_falling:
            self.movey += fall_speed

    # Define player jump
    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True
    
    def stop_jumping(self):
        if self.is_jumping:
            self.is_falling = True
            # @BUG: Possible to jump in the air while falling
            self.is_jumping = False

    # @TODO: Update player 
    def update(self, e_list=None, g_list=None, p_list=None):

        # @TODO: Define collisions with enemies

        # @TODO: Define collisions with ground
        if g_list is not None:
            ground_hit_list = pygame.sprite.spritecollide(self, g_list, False)
            for g in ground_hit_list:
                self.movey = 0
                self.rect.bottom = g.rect.top
                self.is_jumping = False
                self.is_falling = False
    
        # @TODO: Define collisions with platforms
        if p_list is not None:
            plat_hit_list = pygame.sprite.spritecollide(self, p_list, False)
            for p in plat_hit_list:
                self.is_jumping = False
                self.movey = 0

                if self.rect.bottom <= p.rect.bottom:
                    self.rect.bottom = p.rect.top
                    self.is_falling = False
                else:
                    self.gravity()

        # @TODO: Define falling off the world

        # @TODO: Define jumping behaviour

        # @TODO: Update sprite position for moving

        # @TODO: Moving left

        # @TODO: Moving right


class Enemy(pygame.sprite.Sprite):

    # @TODO: Spawn enemy
    def __init__(self, spawnx, spawny, img, img_frames, type, distance, speed, ALPHA=ALPHA):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        self.type = type
        self.distance = distance
        self.speed = speed
        
        for i in range(0,img_frames):
            image = pygame.image.load(os.path.join('assets/', f'{img}{i}.png')).convert()
            image.convert_alpha()
            image.set_colorkey(ALPHA)
            self.images.append(image)
        
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = spawnx
        self.rect.y = spawny
        self.counter = 0

    # @TODO: Set enemy movement
    def move(self):
        pass

    def gravity(self, fall_speed):
        pass


class EnemyFlying(Enemy):

    # @TODO: Overwrite gravity function
    def gravity(self):
        pass

    # @TODO: Set enemy movement
    def fly(self):

        # @TODO: Define flight

        self.move()


class Platform(pygame.sprite.Sprite):
    
    # Spawn platform
    def __init__(self, xloc, yloc, img, ALPHA=ALPHA):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets/', f'{img}.png')).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = xloc
        self.rect.y = yloc


class Level():

    # Initialise level
    def __init__(self, lvl, sizex):
        pygame.sprite.Sprite.__init__(self)
        self.lvl = lvl
        self.sizex = sizex

    # @TODO: Initialise enemy list
    def enemies(self):
        pass

    # Initialize ground list
    def ground(self, tilex, tiley, worldx, worldy, img, ground_height=0):

        # If ground height is not specified, set to tile height
        if ground_height == 0:
            ground_height = worldy - tiley
        
        gloc = []
        gloc.append({
            'x': 0,
            'y': ground_height,
            'w': tilex,
            'length': (worldx/tilex)+tilex,
            'img': img
        })

        self.ground_list = self.platforms(gloc)

        return self.ground_list

    # Initialize platform list
    def platforms(self, ploc):
        # ploc in format {x:0, y:0, w:0, img:0, length:0, optional ALPHA:ALPHA}
        plat_list = pygame.sprite.Group()

        # Check for presence of ALPHA
        if len(ploc) > 0:
            if len(ploc[0]) == 6:
                for p in ploc:
                    if 'ALPHA' in p.keys():
                        i = 0
                        while i <= p['length']:
                            plat = Platform(p['x']+(i*p['w']), p['y'], p['img'], p['ALPHA'])
                            plat_list.add(plat)
                    else:
                        i = 0
                        while i <= p['length']:
                            plat = Platform(p['x']+(i*p['w']), p['y'], p['img'])
                            plat_list.add(plat)
        
        self.plat_list = plat_list

        return self.plat_list
