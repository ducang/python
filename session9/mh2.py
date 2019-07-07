color = ['red','blue','white']
# pos= int(input('enter the position:')) - 1
# print('ur color is:',color[pos])
print('Our color list:')
for i, item in enumerate(color):    
    print(i+1, '.' ,item)
delete = input('Item to delete:')
if delete.isdigit():
    color.pop(int(delete) - 1)
else: color.remove(delete)
for i, item in enumerate(color):
    print(i+1,'.',item)

