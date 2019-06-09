import random
point = 0
running = True
while running:
   
    a = random.randint(-20,20)
    b = random.randint(-20,20)
    coin = random.randint(0,1)
    result = 0
    status = 'true'
    
    if coin == 1:
        result = a+b
    else:
        result = random.randint(-40,40)
        while result == (a+b):
            result = random.randint(-40,40)
        status = 'false'
   
    print (a,'+' ,b ,'=', result)
    ans = str(input('True or false:'))
    
    if ans == status:
        point += 1
        print('Point:', point)
    elif ans == 'exit':
        running = False
    else:
        print ('Lose!!!')
        running = False