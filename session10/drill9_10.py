from random import shuffle
from random import randint
# dic = {
#     'Name of the book' : "Harry Potter And The Sorcerer's Stone",
#     'Release date' : '26/6/1997',
#     'Characters' : ['Harry Potter' , 'Hermione Granger' , 'Ronald Weasley'],
# }

Q = [
    {
    "question": 'What is the name of the first book of J.K Rowling?',
    "choices" : ["Harry Potter And The Sorcerer's Stone" ,
    'Harry Potter And The Prisoner of Azkaban' , 'The Casual Vacancy'],
    "result" : "Harry Potter And The Sorcerer's Stone"

    },
    {
        'question': 'Who is the chosen one in Star Wars?',
        'choices' : ['Qui-Gon Jinn','Anakin Skywalker','Luke Skywalker'],
        'result' : 'Anakin Skywalker'

    },
    {
        'question' : "What was the best-known case of Sherlock Holmes?",
        'choices' : ['The Hound of Baskervilles','The Red-headed League',
        'The Adventure of the Dancing Men'],
        'result' : 'The Adventure of the Dancing Men'
    }
]
point = 0
lenght = len(Q)
while True:
    for question in Q:
        print(question['question'])
        for index, choice in enumerate(question['choices']):
            print(index + 1, choice)
        ans = int(input('Your Answer:'))
        if question['choices'][ans - 1] == question['result']:
            print('Good Job!!!')
            point += 1
            print('Your Point:',point)
        else:
            print('Nice Try')
            break
    percent = point / lenght * 100
    print('percentage of correct answers:', round(percent),'%')
    break

    

    
