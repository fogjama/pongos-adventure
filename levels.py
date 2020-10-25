
def select_level(lvl, worldx, worldy):
    switcher = {
        1: level_1,
        2: level_2
    }

    lvl_func = switcher.get(lvl, lambda: level_1)
    return lvl_func(worldx, worldy)

def level_1(worldx, worldy):
    lvl = '1'
    folder = 'lvl' + lvl + '/'
    background = folder + 'background'
    gloc = {
        'tilex': 125,
        'tiley': 143,
        'worldx': worldx,
        'worldy': worldy,
        'img': folder + 'ground',
        'ground_height': worldy - 50,
        'ALPHA': (0,255,0)
    }

    ploc = []
    ploc.append({
        'x':200,
        'y':worldy-150-100,
        'w':128,
        'length':5,
        'img': folder + 'platform1',
        'ALPHA':(0,255,0)
    })
    ploc.append({
        'x':350,
        'y':worldy - 150 - 200,
        'w':96,
        'length':1,
        'img':folder + 'platform2',
        'ALPHA':(0,255,0)
    })

    return {'ploc': ploc,'gloc': gloc, 'background': background}

def level_2(worldx, worldy):
    lvl = '2'
    folder = 'lvl' + lvl + '/'
    background = folder + 'background'
    gloc = {
        'tilex': 60,
        'tiley': 60,
        'worldx': worldx,
        'worldy': worldy,
        'img': folder + 'ground',
        'ground_height': worldy - 50,
        'ALPHA': (0,0,0)
    }

    ploc = []
    ploc.append({
        'x':250,
        'y':worldy - 200,
        'w':60,
        'length':10,
        'img': folder + 'platform2',
        'ALPHA':(0,0,0)
    })

    return {'ploc': ploc,'gloc': gloc, 'background': background}

if __name__ == "__main__":
    print(select_level(1, 800, 600))
