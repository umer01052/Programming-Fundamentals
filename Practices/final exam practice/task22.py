def is_sorted(x, length):
    for i in range( length):
        if x[i ] > x[i+1]:
            return False
    return True
from random import *
length = randint(5, 15)
x = [0] * length
for i in range(length):
    
    x[i] = randint(0, 100)
    print (x[i], end = ' ')
print()
f=is_sorted(x,length)
if f:
    print('list is sorted')
else:
    print('list is  not sorted')
