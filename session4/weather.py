import random

a= random.randint(0,100)
print(a)
if a < 30:
    print('rainy')
elif 30 <= a and a<60:
    print('cloudy')
else:
    print('sunny')