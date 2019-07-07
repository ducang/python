district = ['ST','BD','BTL','CG','DD','HBT']
population = [150300 , 247100 , 333300 , 266800 , 420900 , 318000]
area = [117.43 , 9.224 , 43.35 , 12.04 , 9.96 , 10.09]

dens = []

for i, value in enumerate(population):
    density = value / area[i]
    dens.append(density)

# print(dens)

sum = sum(dens)
ln = len(district)

avg_dens = sum / ln

print(avg_dens)


    
