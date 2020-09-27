import pygame
from objects import Level


def select_level(lvl):
    switcher = {
        1: level_1,
        2: level_2
    }

    lvl_func = switcher.get(lvl, lambda: print('Level does not exist'))
    lvl_func()

def level_1():
    print('Level 1')

def level_2():
    print('Level 2')