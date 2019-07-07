# items = ['sport','lol','bts','death note','netflix']

# for i, item in enumerate(items):
#     print(i+1,'.',item.upper())

items = ['sport','lol','bts','death note','netflix']
for i in items:
    char = list(i)
    found = False
    for j in char:
        if j == "e" or j == "E":
            found = True
    if found == True:
        print(i)