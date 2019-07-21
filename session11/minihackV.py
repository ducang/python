lap = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}

# lap['Dell'] = 60
# lap['Macbook'] = 2
# lap['Toshiba'] = 10
# lap['Alienware'] = 5
# lap['Fujitsuba'] = 15

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

brand = input('brand:')
quant = int(input('Quantity left:'))

# cost = quant * price[brand.upper()]
# print('$',cost)

deli = lap[brand.upper()] - quant
cost = deli * price[brand.upper()]

print('Inventory delivery note:','\n', brand,':',deli,';','Total:',cost)