import datetime
import time

month = int(input(""))
a = [2,4,6,9,11]
b = [1,3,5,7,8,10,12]
year = int(input(""))

while True:
    if month > 13:
        print('re-enter')
        month = int(input(""))
    else:
        if month in a:
            if month == 2 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                print("29") 
            else: print("28") 
            if month != 2:
                print("30")
        else: print("31") 
    break
    