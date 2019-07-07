stranger_things = {
    'name' : 'stranger things',
    'release date' : '15 July 2016',
    'seasons' : 3,
    'imdb' : 8.9,
    'rotten tomatoes' : '95%',
    'genre' : 'horror',
}

print(stranger_things)

key = input('select key to update:')
content = input('update content:')

stranger_things[key] = content

print(stranger_things)