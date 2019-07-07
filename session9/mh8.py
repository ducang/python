while True:
    h_scores = [ 45 , 67 , 56 , 78 ]

    for i in range( len(h_scores) ):
        for j in range( i+1, len( h_scores ) ):
            if h_scores[i] < h_scores[j]:
                tmp = h_scores[i]
                h_scores[i] = h_scores[j]
                h_scores[j] = tmp

    for k, value in enumerate(h_scores):
        print(k+1, '.' , value)

    new_hsr = int(input('Enter your new score:'))
    h_scores.append(new_hsr)

    for i in range( len(h_scores) ):
        for j in range( i+1, len( h_scores ) ):
            if h_scores[i] < h_scores[j]:
                tmp = h_scores[i]
                h_scores[i] = h_scores[j]
                h_scores[j] = tmp

    for k, value in enumerate(h_scores):
        print(k+1, '.' , value)

    break




