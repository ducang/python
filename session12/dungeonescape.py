from random import randint
while True:
    map = [
        ['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']
    ]
    
    px = randint(0,3)
    py = randint(0,3)
    kx = randint(0,3)
    ky = randint(0,3)
    ex = randint(0,3)
    ey = randint(0,3)
    
    
    while px == ky or kx == ey or py == ex :
        px = randint(0,3)
        kx = randint(0,3)
        ex = randint(0,3)
        py = randint(0,3)
        ky = randint(0,3)
        ey = randint(0,3)
        
    map[px][py] = 'P'
    map[kx][ky] = 'K'
    map[ex][ey] = 'E'
    
    # STATUS
    found = False
    # PROCESS
    while True:
        map[ex][ey] = 'E'
        
        for i in map:
            print(*i)
        move = input('Your move:')
        if move == 'w':
            if px > 0:
                px -= 1
            map[px][py] = 'P'
            map[px + 1][py] = '_'     
        elif move == 's':
            if px < 3:
                px += 1
            map[px][py] = 'P'
            map[px - 1][py]= '_'
        elif move == 'a':
            if py > 0:
                py -= 1
            map[px][py] = 'P'
            map[px][py+1] = '_'
        elif move == 'd':
            if py < 3:
                py += 1
            map[px][py] = 'P'
            map[px][py - 1] = '_'
        if map[px][py] == map[kx][ky]:
            found = True
            print('You got the key!')
        if map[px][py] == map[ex][ey] and found == True:
            print('Good Job!','You just escaped the dungeon')
            break
        elif map[px][py] == map[ex][ey] and found == False:
            print('You must get the key first!')

        

