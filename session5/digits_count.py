"""dem digit"""       
while True:
    a= int(input("Enter a number:"))

m = int(input("enter a number:"))
c = 0
while (m>0):
    m = m//10
    c = c+1   
if c<=1:
    print("your number has",c,"digit")
else:
   print("your number has",c,"digits")