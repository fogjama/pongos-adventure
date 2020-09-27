
def select_level(lvl, worldx, worldy):
    switcher = {
        1: level_1,
        2: level_2
    }

    lvl_func = switcher.get(lvl, lambda: level_1)
    return lvl_func(worldx, worldy)

def level_1(worldx, worldy):
    background = 'stage'
    gloc = {
        'tilex': 0,
        'tiley': 0,
        'worldx': worldx,
        'worldy': worldy,
        'img': '',
        'ground_height': 0
    }

    ploc = []
    ploc.append({
        'x':0,
        'y':0,
        'w':0,
        'length':0,
        'img':'',
        'ALPHA':(0,255,0)
    })

    return {'ploc': ploc,'gloc': gloc, 'background': background}

def level_2(worldx, worldy):
    background = 'stage1'
    gloc = {
        'tilex': 0,
        'tiley': 0,
        'worldx': worldx,
        'worldy': worldy,
        'img': '',
        'ground_height': 0
    }

    ploc = []
    ploc.append({
        'x':0,
        'y':0,
        'w':0,
        'length':0,
        'img':'',
        'ALPHA':(0,255,0)
    })

    return {'ploc': ploc,'gloc': gloc, 'background': background}

if __name__ == "__main__":
    print(select_level(1, 800, 600))
