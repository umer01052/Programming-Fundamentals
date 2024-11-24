import random
rows=int(input('Enter rows: '))
columns=int(input('Enter columns: '))

for i in range(rows):
    for j in range(columns):
        n=random.randint(1,9)
        print(n,end=" ")
    print()
