import random


rows = 4
cols = 3
matrix= [[random.randint(10, 50) for j in range(cols)] for i in range(rows)]


print("Elements in a single line:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
print()


print("Elements in tabular form:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ') 
    print()


print("Elements in row-column format:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=' ')
    print()
