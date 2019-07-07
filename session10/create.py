stranger_things = {
    'name' : 'stranger things',
    'seasons' : 3,
    'imdb' : 8.9
}

print(stranger_things)

stranger_things['release date'] = '15 Jul 2016'

print(stranger_things)  

add0 = input('enter title:')
add1 = input('enter content:')

stranger_things[add0] = add1

print(stranger_things)

key = input('enter the key:')

print(stranger_things[key])