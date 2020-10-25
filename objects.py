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
            self.movey = 0
            self.is_falling = False
            self.is_jumping = True
    
    def stop_jumping(self):
        if self.is_jumping:
            self.is_falling = True
            # @BUG: Possible to jump in the air while falling
            self.is_jumping = False

    # Update player 
    def update(self, ani, e_list=None, g_list=None, p_list=None, worldy=0):

        # @TODO: Define collisions with enemies

        # Define collisions with ground
        if g_list is not None:
            ground_hit_list = pygame.sprite.spritecollide(self, g_list, False)
            for g in ground_hit_list:
                if self.is_jumping and self.is_falling is False:
                    self.movey = 0
                else:
                    self.movey = 0
                    self.rect.bottom = g.rect.top + self.fall_speed
                    self.is_jumping = False
                    self.is_falling = False
    
        # Define collisions with platforms
        if p_list is not None:
            plat_hit_list = pygame.sprite.spritecollide(self, p_list, False)
            for p in plat_hit_list:
                if self.is_jumping and self.is_falling is False:
                    self.movey = 0
                    self.gravity()
                else:
                    self.is_jumping = False
                    self.movey = 0

                    if self.rect.bottom <= p.rect.bottom:
                        self.rect.bottom = p.rect.top + self.fall_speed
                        self.is_falling = False
                    else:
                        self.gravity()

        # Define falling off the world
        if worldy > 0:
            if self.rect.y > worldy:
                self.health -= 1

                # @TODO: Allow for falling off the world in either direction
                self.rect.x = self.rect.x + 50

                if worldy >= 200:
                    self.rect.y = worldy - 200
                else:
                    self.rect.y = worldy

        # Define jumping behaviour
        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 33

        # Update sprite position for moving
        if self.rect.x > (0 + self.movex) or self.movex > 0:
            self.rect.x += self.movex
        self.rect.y += self.movey

        # Moving left
        if self.movex < 0:
            self.is_falling = True
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame//ani],True,False)

        # Moving right
        if self.movex > 0:
            self.is_falling = True
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

class Enemy(pygame.sprite.Sprite):

    # Spawn enemy
    def __init__(self, spawnx, spawny, img, img_frames, type, distance, speed, ALPHA=ALPHA, fall_speed=6):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        self.type = type
        self.distance = distance
        self.speed = speed
        self.fall_speed = fall_speed
        self.movey = 0
        
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

    # Set enemy movement
    def move(self, ani):
        if self.counter >= 0 and self.counter < self.distance:
            self.rect.x += self.speed
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
        elif self.counter >= self.distance and self.counter < self.distance*2:
            self.rect.x -= self.speed
            self.frame += 1
            if self.frame > 3* ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame//ani],True,False)
        else:
            self.counter = 0
        
        self.counter += 1

    def gravity(self, fall_speed=0, g_list=None, p_list=None):
        if fall_speed == 0:
            fall_speed = self.fall_speed

        self.rect.y += fall_speed

        if g_list is not None:
            g_hit_list = pygame.sprite.spritecollide(self,g_list,False)
            for g in g_hit_list:
                self.rect.bottom = g.rect.top
        if p_list is not None:
            p_hit_list = pygame.sprite.spritecollide(self,p_list,False)
            for p in p_hit_list:
                if self.rect.bottom <= p.rect.bottom:
                    self.rect.bottom = p.rect.top


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


class Level:

    # Initialise level
    def __init__(self, lvl, sizex, backscroll):
        pygame.sprite.Sprite.__init__(self)
        self.lvl = lvl
        self.sizex = sizex
        self.ground_list = pygame.sprite.Group()
        self.plat_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

        self.settings_values(200,200,30,4,backscroll)

    # @TODO: Initialise enemy list
    def enemies(self, eloc):
        # eloc as [] with elements in formatn {x:0, y:0, img:string, frames:4, type:string, distance:20, speed:5, ALPHA:(0,0,0), fall_speed:6}
        new_enemy_list = pygame.sprite.Group()

        if len(eloc) > 0:
            for e in eloc:
                enemy = Enemy(
                    e['x'],
                    e['y'],
                    e['img'],
                    e['img_frames'],
                    e['type'],
                    e['distance'],
                    e['speed'],
                    e['ALPHA'],
                    e['fall_speed']
                        )
                new_enemy_list.add(enemy)
        self.enemy_list = new_enemy_list


    # Initialize ground list
    def ground(self, tilex, tiley, worldx, worldy, img, ground_height=0, alpha_value=ALPHA):

        # If ground height is not specified, set to tile height
        if ground_height == 0:
            ground_height = worldy - tiley
        
        gloc = []
        gloc.append({
            'x': 0,
            'y': ground_height,
            'w': tilex,
            'length': (worldx/tilex)+tilex,
            'img': img,
            'ALPHA': alpha_value 
            # Doesn't seem to generate without specifying ALPHA value
            # @TODO: Figure out why optional ALPHA doesn't seem to be optional
        })

        self.ground_list = self.create_platforms(gloc)
    

    def platforms(self, ploc):
        self.plat_list = self.create_platforms(ploc)

    # Initialize platform list for ground or platforms
    def create_platforms(self, ploc):
        # ploc [] with elements in format {x:0, y:0, w:0, img:0, length:0, optional ALPHA:ALPHA}
        new_plat_list = pygame.sprite.Group()
        # Check for presence of ALPHA
        if len(ploc) > 0:
            if len(ploc[0]) == 6:
                for p in ploc:
                    if 'ALPHA' in p.keys():
                        i = 0
                        while i < p['length']:
                            plat = Platform(p['x']+(i*p['w']), p['y'], p['img'], p['ALPHA'])
                            new_plat_list.add(plat)
                            i += 1
                    else:
                        i = 0
                        while i < p['length']:
                            plat = Platform(p['x']+(i*p['w']), p['y'], p['img'])
                            new_plat_list.add(plat)
                            i += 1
        
        return new_plat_list
    
    def settings_values(self,forwardx,backwardx,fps,ani,backscroll=False):
        self.forwardx = forwardx
        self.backwardx = backwardx
        self.fps = fps
        self.ani = ani
        self.backscroll = backscroll
