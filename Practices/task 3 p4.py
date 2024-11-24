import random
x=random.randint(1,10)
y=random.randint(1,10)
z=random.randint(1,10)
print('First Number',x)
print('Second Number',y)
print('Third Number',z)
if x-y==2 or x-y==-2 and y-z==2 or y-z==-2 and x-z==2 or x-z==-2 :
    print('OK')
else:
    print('Sorry')
