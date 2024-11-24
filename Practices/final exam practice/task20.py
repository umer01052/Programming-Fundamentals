from random import *
length = randint(5, 15)
x1= [0] * length
for i in range(length):
    
    x1[i] = randint(0, 100)
print("List1:",*x1)
x2= [0] * length
for i in range (length):
    x2[i] = randint(0, 100)
print("List2:",*x2)
for i in range (length):
    if x1[i]>x2[i]:
        print(x1[i],end=' ')
    else:
        print(x2[i],end=' ')
