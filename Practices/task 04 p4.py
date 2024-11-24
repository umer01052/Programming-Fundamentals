import random
x1=random.randint(1,100000)
x2=random.randint(1,100000)
x3=random.randint(1,100000)
x4=random.randint(1,100000)
print('Number Before Sorting')
print(f' N1={x1}  N2={x2}  N3={x3}  N4={x4}')
if x1>x2:
    x1,x2=x2,x1
if x2>x3:
    x2,x3=x3,x2
if x3>x4:
    x3,x4=x4,x3
if x1>x2:
    x1,x2=x2,x1
if x2>x3:
    x2,x3=x3,x2
if x1>x2:
    x1,x2=x2,x1
print('Number After Sorting')
print(f' N1={x1}  N2={x2}  N3={x3}  N4={x4}')


