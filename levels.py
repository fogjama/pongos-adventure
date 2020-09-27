import pygame
from objects import Platform


def generate_simple_ground(tilex, tiley, worldx, worldy, img, ground_height=0):

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

    ground_list = generate_platforms(gloc)

    return ground_list


def generate_platforms(ploc):
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
    
    return plat_list
    


