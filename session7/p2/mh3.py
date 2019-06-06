odd = int(input(""))
r = range(odd,0,-2)
a = odd%2
if a==1:
    print(*r,"0")
else:
    print("w")