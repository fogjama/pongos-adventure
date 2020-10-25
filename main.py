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
                    
                # Quit game
                if event.key == K_ESCAPE:
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        game = False
        
        world.blit(home_backdrop, backdropbox)
        pygame.display.flip()

def stats(level,score,health,world,colour):
    if level.myfont is not None:
        level.myfont.render_to(world, (4, 4), 'Score: '+str(score), colour, None)
        level.myfont.render_to(world, (4, 50), 'Health: '+str(health), colour, None)

def start_level(lvl, hero, fps, worldx, worldy, world, clock):
    main = True

    # Set level data for chosen level
    level_data = select_level(lvl, worldx, worldy)

    # Initialise level class based on level data
    current_level = Level(
        lvl,
        worldx,
        level_data['backscroll'],
        font_path=level_data['font_file'],
        font_size=level_data['font_size'])

    # Set level settings values
    current_level.settings_values(worldx - 200,200,30,4)

    # Create backdrop for current level
    backdrop = pygame.image.load(os.path.join('assets/', level_data["background"] + '.png'))
    backdropbox = world.get_rect()

    # Create hero
    # @TODO: Move hero creation to main game function and pass into levels
    hero = Player(0,0,10,10,hero[0],hero[1],hero[2])
    player_list = pygame.sprite.Group()
    player_list.add(hero)

    # Create ground
    current_level.ground(
        level_data['gloc']['tilex'],
        level_data['gloc']['tiley'],
        level_data['gloc']['worldx'],
        level_data['gloc']['worldy'],
        level_data['gloc']['img'],
        level_data['gloc']['ground_height'],
        level_data['gloc']['ALPHA'])
    
    ground_list = current_level.ground_list

    # Create platforms
    current_level.platforms(level_data['ploc'])
    plat_list = current_level.plat_list

    # @TODO: Set dynamic walk speed
    steps = 10


    # Create enemies
    current_level.enemies(level_data['eloc'])
    enemy_list = current_level.enemy_list

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
                    # Move player left
                    hero.move(-steps,0)
                if event.key == K_RIGHT or event.key == ord('d'):
                    # Move player right
                    hero.move(steps,0)
                if event.key == K_UP or event.key == ord('w') or event.key == K_SPACE:
                    # Jump
                    hero.jump()
            
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == ord('a'):
                    # Stop left movement
                    hero.move(steps,0)
                if event.key == K_RIGHT or event.key == ord('d'):
                    # Stop right movement
                    hero.move(-steps,0)
                if event.key == K_UP or event.key == ord('w') or event.key == K_SPACE:
                    # Stop jump
                    hero.stop_jumping()
                
                if event.key == K_ESCAPE:
                    # pygame.quit()
                    # try:
                    #     sys.exit()
                    # finally:
                    #     main = False
                    main = False
                
        
        # Scrolling
        if hero.rect.x >= current_level.forwardx:
            scroll = hero.rect.x - current_level.forwardx
            hero.rect.x = current_level.forwardx
            for p in plat_list:
                p.rect.x -= scroll
            for g in ground_list:
                g.rect.x -= scroll
            for e in enemy_list:
                e.rect.x -= scroll
        
        # @TODO: Implement backscroll

        
        world.blit(backdrop, backdropbox)
        hero.gravity(3.2)
        hero.update(current_level.ani,e_list=enemy_list,g_list=ground_list,p_list=plat_list,worldy=worldy)
        player_list.draw(world)

        # draw enemies
        enemy_list.draw(world)

        # Initialise enemy movement
        for e in enemy_list:
            e.gravity(g_list=ground_list,p_list=plat_list)
            e.move(current_level.ani)

        # draw ground
        ground_list.draw(world)
        # draw platforms
        plat_list.draw(world)

        # Initialise text
        stats(current_level,hero.score,hero.health,world,level_data['font_colour'])

        if hero.health == 0:
            main = False

        pygame.display.flip()
        clock.tick(fps)


create_game(800,600,'stage',['hero',8,(0,255,0)])