vari = ['a','b','c']
vari[2] = input('nhap variable moi:')  
print(*vari,sep=',')
vari.pop(1)
print(*vari, sep=',')

# found = False
# a = input('thu can xoa:')
# things = ['sport','lol','bts']
# for i in things:
#     if i == "lol":
#         found = True
# if found == True:
#     things.remove(a)
# print(things)

# found = False
# a = int(input('vi tri thu can xoa:'))
# things = ['sport','lol','bts']
# for i in things:
#     if i == "lol":
#         found = True
# if found == True:
#     things.pop(a)
# print(things)