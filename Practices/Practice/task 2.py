from random import*
x1 = randint(1,1000)
x2 = randint(1,1000)
x3 = randint(1,1000)
x4 = randint(1,1000)
print (x1, x2, x3, x4)

if x1 > x2:
     x1,x2 = x2,x1
if x2 > x3:
    x2, x3 = x3,x2
if x3 > x4:
    x3, x4 = x4 ,x3

print (x1, x2, x3, x4)



