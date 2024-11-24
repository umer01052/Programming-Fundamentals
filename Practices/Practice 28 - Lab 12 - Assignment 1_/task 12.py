import random
list=[0]*10
for i in range(10):
    list[i]=random.randint(3,7)
print(*list)

for i in range (len(list)):
    sum=0
    if i >=1:
        for j in range (i):
            print(list[j],end=" ")
            sum=sum+list[j]
        print('=',end=" ")
        print(sum,end=" ")
        print()
