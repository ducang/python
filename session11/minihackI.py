lap = {
    'HP' : 20,
    'Dell' : 50,
    'Macbook' : 12,
    'Asus' : 30
}

read = input('Your brand:')
if read.upper() == 'HP':
    print('Quantity:', lap['HP'])
elif read.capitalize() in lap:
    print('Quantity:',lap[read.capitalize()])