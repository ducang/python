from random import randint
char = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}

char['Gold'] = 150
char['Backpack'].append('Flint Stone')
char['Pocket'] = ['MonsterDex' , 'Flashlight']

skill =[
    {
        'Name' : 'Tackle',
        'Minimum level': 1,
        'Damage' : 5,
        'Hit rate' : 0.3,
    },
    {
        'Name': 'Quick attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5,
    },
    {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2,
    }
]

# print(skill)

print('Choose your action:')
for i,j in enumerate(skill):
    print(i+1,'.',j['Name'])



print('Your enemy ahead!!')
hp = 100
print('Enemy HP =',hp)
while True:
    coin = randint(0,1)
    action = int(input('Enter your action:'))
    if char['Level'] >= skill[action - 1]['Minimum level']:
        if coin >= skill[action - 1]['Hit rate']:
            print('Damage dealt:',skill[action - 1]['Damage'])
            hp -= skill[action - 1]['Damage']
            print('Enemy HP =',hp)
        else:
            print('Miss!')
        char['HP'] -= skill[1]['Damage']
        print('Enemy used quick attack','\n','HP lost:',skill[1]['Damage'],'\n','Your HP:', char['HP'])
        
    else:
        print('Not learned yet')
    