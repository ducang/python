h_scores = [ 45 , 67 , 56 , 78 ]

for i, value in enumerate(h_scores):
    print(i+1 , '.' , value)

new_hsr = int(input('Enter your new score:'))

h_scores.append(new_hsr)

for i, value in enumerate(h_scores):
    print(i+1 , '.' , value)

