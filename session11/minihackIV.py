lap = {
    'HP' : 20,
    'Dell' : 50,
    'Macbook' : 12,
    'Asus' : 30
}
lap['Dell'] = 60
lap['Macbook'] = 2
lap['Toshiba'] = 10
lap['Alienware'] = 5
lap['Fujitsuba'] = 15

price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJITSU': 900,
    'ALIENWARE': 1000
}
# print(price['ASUS'])

brand = input('brand:')
print(price[brand.upper()])