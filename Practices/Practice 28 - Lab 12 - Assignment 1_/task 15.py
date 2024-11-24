import random
Len=10
list= [[random.randint(0, 9) for j in range(Len)] for i in range(Len)]
for row in list:
    for elements in row:
        print(elements, end=' ')
    print()
print()

for i in range (Len):
    for j in range (Len):
        if list[i][j]==0:
            list[i][j]=1
        
for row in list:
    for elements in row:
        print(elements, end=' ')
    print()
