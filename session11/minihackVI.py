lap = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}

lap['DELL'] = 60
lap['MACBOOK'] = 2
lap['ACER'] = 0
lap['Toshiba'] = 10
lap['Fujitsu'] = 15
lap['Alienware'] = 5


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
sum = 0
for i,j in lap.items():
    print(i,'quantity:',lap[i]) 
    a = price[i.upper()] * lap[i]
    print('Total: $',a,'\n')
    sum += a
print('Total of warehouse: $',sum)
    



