file = open("records.txt","r")
best_average =0
high_score = 0
i = 1
num_of_players = int(file.readline())
while i<=num_of_players:
    score = 0
    y = 1
    no_of_matches = int(file.readline())
    print(f'Player {i} score:', end = " ")
    while y <=no_of_matches:
        score = int(file.readline())
        print(score,end = ' ')
        if (score>high_score):
            high_score = score
        
        score = score+score
       
        y = y+1
    print()
    average = score/no_of_matches
    print("Average: ",average)
    if (average>best_average):
        best_average= average

    i+=1
    print('Best Average',best_average)
    print('High score',high_score)
