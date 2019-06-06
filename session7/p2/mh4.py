from turtle import *

side = int(input(""))
a= 360/side
shape("turtle")

for i in range(side):
    forward(100)
    left(a)
    speed(-1)
mainloop()