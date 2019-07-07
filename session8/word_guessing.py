from random import shuffle
from random import choice
fruit = ['apple', 'orange', 'grape', 'guava']
point = 0
while True:

    i = choice(fruit)

    if i == 'apple':

        char = list(i)
        shuffle(char)
        print(*char,'\n', sep='')
        a = input('what is it?')
        
        if a == 'apple':
            print('correct')
            point +=1
            print('Point:',point,'\n')
        else:
            print('lose')
            break
    elif i == 'orange':

        char = list(i)
        shuffle(char)
        print(*char,'\n', sep='')
        a = input('what is it?')
        
        if a == 'orange':

            print('correct')
            point +=1
            print('Point:',point,'\n')

        else:

            print('lose')
            break
    elif i == 'grape':

        char = list(i)
        shuffle(char)
        print(*char,'\n', sep='')
        a = input('what is it?')
        
        if a == 'grape':

            print('correct')
            point += 1
            print('Point:',point,'\n')

        else:
            print('lose')
            break

    elif i == 'guava':

        char = list(i)
        shuffle(char)
        print(*char,'\n', sep='')
        a = input('what is it?')
        
        if a == 'guava':

            print('correct')
            point += 1
            print('Point:',point,'\n')

        else:

            print('lose')
            break

    else:
        
        break