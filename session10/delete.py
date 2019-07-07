stranger_things = {
    'name' : 'stranger things',
    'release date' : '15 July 2016',
    'seasons' : 3,
    'imdb' : 8.9,
    'rotten tomatoes' : '95%',
    'genre' : 'horror',
}

print(stranger_things)

delete = input('enter key to delete:')

del stranger_things[delete]

print(stranger_things)