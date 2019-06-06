import random
point = 0
while True:
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    sum = random.randint(-20,20)
    if (b >= 0):
        print (a ,'+',b,'=', sum)
    else:
        print (a,b,'=',sum)  
    ans = input("True or False:")
    if sum == a+b:
        if ans == 'true':
            point += 1
            print('point:',point)           
        else:
            print("Lose!!!")
            break
    else:
        if ans == 'false':
            point += 1
            print('point:',point)
        else:
            print('Lose!!!')
            break