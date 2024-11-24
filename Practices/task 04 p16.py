import random
rows=int(input('Enter Value: '))
columns=int(input('Enter Value: '))
i=1
while i<=columns:
    x=random.randint(1,9)
    y=1
    while y<=rows:
        print(x, end='')
        
        y+=1
    print()
    i+=1
