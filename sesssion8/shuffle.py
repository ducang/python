import random
word = input('enter a word:')
char = list(word)
random.shuffle(char)
for i in char:
    print(i)

