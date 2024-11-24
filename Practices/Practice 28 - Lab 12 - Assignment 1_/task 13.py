import random
list=[0]*10
for i in range(10):
    list[i]=random.randint(3,7)
print(*list)

for i in range (len(list)):
   
    if i<8:
        k=i
        for j in range (3):
            print(list[k],end=" ")
            k+=1
        print()
