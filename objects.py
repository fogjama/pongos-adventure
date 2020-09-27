import pygame
from pygame.locals import *

ALPHA = (255,255,255)

class Player(pygame.sprite.Sprite):

    # @TODO: Spawn player
    def __init__(self):
        pass

    # @TODO: Control player movement
    def move(self):
        pass

    # @TODO: Define player gravity
    def gravity(self):
        pass

    # @TODO: Define player jump
    def jump(self):
        pass

    # @TODO: Update player 
    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):

    # @TODO: Spawn enemy
    def __init__(self):
        pass

    # @TODO: Set enemy movement
    def move(self):
        pass


class EnemyFlying(Enemy):

    # @TODO: Set enemy movement
    def fly(self):

        # @TODO: Define flight

        self.move()


class Platform(pygame.sprite.Sprite):
    
    # @TODO: Spawn platform
    def __init__(self):
        pass


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
