import random


matrix = [[random.randint(10,99) for j in range(3)] for i in range(4)]

for i in range(4):
    for j in range(3):
        print(matrix[i][j],end=' ')
print()

for i in range (4):
    sum=0
    for j in range (3):
        sum+=matrix[i][j]
        
        print(matrix[i][j],end=" ")
    print('=',end=" ")
    print(sum,end='')
    print()
