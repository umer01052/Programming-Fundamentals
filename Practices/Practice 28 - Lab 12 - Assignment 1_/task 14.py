import random
Len=10
list= [[random.randint(0, 9) for j in range(Len)] for i in range(Len)]
for row in list:
    for elements in row:
        print(elements, end=' ')
    print()

