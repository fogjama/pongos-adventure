import pygame
from pygame.locals import *
from objects import ALPHA, Player, Level
from levels import *
import os
import sys

def create_game(worldx, worldy, backdrop, hero=['hero',8,ALPHA], lvl=1, tilex=32, tiley=32, fps=30):
    clock = pygame.time.Clock()
    pygame.init()

    world = pygame.display.set_mode([worldx, worldy])
    backdropbox = world.get_rect()

    home_backdrop = pygame.image.load(os.path.join('assets/','menu.png'))

    game = True

    while game == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    game = False
            
            if event.type == KEYDOWN:
                # Select level
                if event.key == ord('1'):
                    start_level(1, hero, fps, worldx, worldy, world, clock)
                if event.key == ord('2'):
                    start_level(2, hero, fps, worldx, worldy, world, clock)
                    
                # Quite game
                if event.key == K_ESCAPE:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        game = False
        
        world.blit(home_backdrop, backdropbox)
        pygame.display.flip()

def start_level(lvl, hero, fps, worldx, worldy, world, clock):
    main = True
    level_data = select_level(lvl, worldx, worldy)
    backdrop = pygame.image.load(os.path.join('assets/', level_data["background"] + '.png'))
    backdropbox = world.get_rect()

    hero = Player(0,0,10,10,hero[0],hero[1],hero[2])
    player_list = pygame.sprite.Group()
    player_list.add(hero)

    # @TODO: Create ground_list
    # @TODO: Create plat_list

    # @TODO: Set dynamic walk speed
    steps = 10

    # main = True

    while main == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    # @TODO: Move player left
                    print('left')
                if event.key == K_RIGHT or event.key == ord('d'):
                    # @TODO: Move player right
                    print('right')
                if event.key == K_UP or event.key == ord('w') or event.key == K_SPACE:
                    # @TODO: Jump
                    print('jump')
            
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == ord('a'):
                    # @TODO: Stop left movement
                    print('left stop')
                if event.key == K_RIGHT or event.key == ord('d'):
                    # @TODO: Stop right movement
                    print('right stop')
                if event.key == K_UP or event.key == ord('w') or event.key == K_SPACE:
                    # @TODO: Stop jump
                    print('jump stop')
                
                if event.key == K_ESCAPE:
                    # pygame.quit()
                    # try:
                    #     sys.exit()
                    # finally:
                    #     main = False
                    main = False
                
        
        # @TODO: Implement scrolling

        world.blit(backdrop, backdropbox)
        hero.gravity(3.2)
        player_list.draw(world)
        # @TODO: draw enemies
        # @TODO: Initialise enemy movement
        # @TODO: draw ground
        # @TODO: draw platforms

        hero.update()
        pygame.display.flip()
        clock.tick(fps)

create_game(800,600,'stage',['hero',8,(0,255,0)])