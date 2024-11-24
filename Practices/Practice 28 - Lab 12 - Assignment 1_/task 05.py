import random
list=[0]*10
for i in range(10):
    list[i]=random.randint(1,55)
print(list)
odd=[]
even=[]
for i in range (len(list)):
    if list[i]%2==0:
       even1=list[i]
       even.append(even1)
    else:
       odd1=list[i]
       odd.append(odd1)
print("Even = ",even)
print("Odd = ",odd)

if len(even)>len(odd):
    for i in range (len(list)):
        if list[i] % 2 != 0:
            list[i] -= 1
else:
    for i in range (len(list)):
        if list[i] % 2== 0:
            list[i] += 1
print(*list)
