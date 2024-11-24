from random import *
length = randint(5, 15)
x = [0] * length
for i in range(length):
    
    x[i] = randint(0, 100)
    print (x[i], end = ' ')
print()
for i in range (length-1):
    if x[i]>x[i+1]:
        print(x[i],end=',')
        print(x[i+1],end=' ')
        print()
