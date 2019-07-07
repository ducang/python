color = ['red','blue','white']
print('Our color list:')
print(*color,sep=',')
color.append(input('Enter new color:'))
print('New color list:') 
print(*color,sep=',')