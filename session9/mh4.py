# number = [1,4,19,40,12,15]
# length = len(number)
# i = 0
# while i < length:
#     for i in number:     
#         if i % 2 == 0:
#             print(i, end=' ')
#         else:
#             i += 1

n = input('enter numbers, separated by , :')
n1 = n.split(',')
length = len(n1)
i = 0
while i < length:
    if int(n1[i]) % 2 == 0:
        print(n1[i])
    i += 1
            

