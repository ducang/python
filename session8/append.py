menu = ['Sterloin', 'Tenderloin' , 'Rib Eyes']
print(menu, sep =',')
menu.append(input('Add new dish:'))
lenght = len(menu)
print( menu[0].upper() ,menu[lenght - 2].upper(), menu[lenght - 1].upper(), sep=',' )
