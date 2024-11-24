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
small=[]
large=[]
for i in range (length):
    if x1[i]>x2[i]:
        large.append(x1[i])
        small.append(x2[i])
    else:
        small.append(x1[i])
        large.append(x2[i])
print("Smaller",*small)
print("LArger",*large)
