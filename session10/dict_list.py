dic = {
    'Name of the book' : "Harry Potter And The Sorcerer's Stone",
    'Release date' : '26/6/1997',
    'Characters' : ['Harry Potter' , 'Hermione Granger' , 'Ronald Weasley'],
}

# print(dic)

dic['Country'] = 'UK'

# print(dic)   

# for k,v in dic.items():
#     print(k,'-',v)

dic['Characters'] = ['Hagrid' , 'Albus' , 'Draco']
dic['Characters'].append('Neville')
# dic['Characters'].pop(0)
# print(dic)
# print(dic['Characters'][1])

# for i in dic['Characters']:
#     print(i)

for k,v in dic.items():
    print(k , '-' ,v)