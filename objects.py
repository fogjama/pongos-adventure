import pygame
from pygame.locals import *
import os

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
    def gravity(self, fall_speed):
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
            self.is_jumping = False

    # @TODO: Update player 
    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):

    # @TODO: Spawn enemy
    def __init__(self, spawnx, spawny, img, img_frames, type, ALPHA=ALPHA):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        self.type = type
        
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
    
    # @TODO: Spawn platform
    def __init__(self, xloc, yloc, imgw, imgh, img, ALPHA=ALPHA):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets/', f'{img}.png')).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = xloc
        self.rect.y = yloc


class Level():

    # @TODO: Initialise level
    def __init__(self, lvl, sizex, env):
        pygame.sprite.Sprite.__init__(self)
        self.lvl = lvl
        self.sizex = sizex
        self.env = env

    # @TODO: Initialise enemy list
    def enemies(self):

        pass

    # @TODO: Initialise platform list
    def platform(self):
        pass

    # @TODO: Initialize ground list
    def ground(self):
        pass
