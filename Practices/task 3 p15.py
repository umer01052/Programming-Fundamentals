import random
i=1
cout=0
cout1=0
max=0
min=1000
while i<=10:
    n1=random.randint(1,1000)
    n2=random.randint(1,1000)
    n3=random.randint(1,1000)
    average=n1+n2+n3/3
    print('Average is', average)
    if average>max:
        max=average
        cout=i
   
    if average<min:
        min=average
        cout1=i
    i+=1
print(f'set of {cout} has maximum average')
print(f'set of {cout1} has minimum average')
