from random import randint
map = [
    ['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']
]
pos = randint(0,3)
pos2 = randint(0,3)
pos3 = randint(0,3)
'''check pos'''
while pos == pos2 or pos == pos3 or pos3 == pos2:
    pos = randint(0,3)
    pos2 = randint(0,3)
    pos3 = randint(0,3)
'''Vi tri cua Player'''
px = pos
py = pos
'''Vi tri cua Key'''
kx = pos2
ky = pos2
'''Vi tri cua Escape'''
ex = pos3
ey = pos3
'''Toa do'''
map[px][py] = 'P'
map[kx][ky] = 'K'
map[ex][ey] = 'E'
'''status cua key'''
found = False
'''code process game'''
while True:
    map[ex][ey] = 'E'

    for i in map:
        print(*i)

    move = input('Your move:')

    if move == 'w':
        if  px > 0:
            px -= 1
        map[px][py] = 'P'
        map[px + 1][py] = '_'

    elif move == 'a':
        if py > 0:
            py -= 1
        map[px][py] = 'P'
        map[px][py+1] = '_'
    elif move == 's':
        if px < 3:
            px += 1
        map[px][py] = 'P'
        map[px - 1][py]= '_'
    elif move == 'd':
        if py < 3:
            py += 1
        map[px][py] = 'P'
        map[px][py - 1] = '_'
    if map [px][py] == map[kx][ky]:
        found = True
        print('You got the key!')
    if map[px][py] == map[ex][ey] and found == True:
        print('Good Job!','You just escaped the dungeon')
        break
    elif map[px][py] == map[ex][ey] and found == False:
        print('You must get the key first!')

    

