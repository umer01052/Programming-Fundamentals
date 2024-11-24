import random
Len=10
list=[0]*Len
sum=0
for i in range(Len):
    list[i]=random.randint(1,55)
    sum=sum+list[i]
print(list)
print('Sum = ',sum)
