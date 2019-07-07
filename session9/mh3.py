# num = [1, 4, 98, 109]

# inp = int(input('enter a number:'))
# found = False
# i = 0
# length = len(num)
# while i < length:
#     if num[i] == inp:
#         found = True
#         print('Found, position',i+1)
#         break
#     else:    
#         i += 1
# if found == False:
#     print("Not found")

# a = sum(num)
# print(a)        

# sum = 0 
# for i in num:
#     sum += i
# print(sum)

lis = input('enter a list of numbers, separated by _ :')
liss = lis.split(' ')
sum = 0
i = 0
length = len(liss)
while i < length:
    sum += int(liss[i])
    i += 1
print(sum)