districts = ['ST','BD','BTL','CG','DD','HBT']
population = [150300,247100,333300,266800,420900,318000]

minn = min(population)
maxx = max(population)

for i, value in enumerate(population):
    if value == minn:
        print(districts[i], ':' , value)
    if value == maxx:
        print(districts[i], ':' , value)
    

