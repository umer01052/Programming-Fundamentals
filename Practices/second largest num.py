import random
len=int(input('Enter Len: '))
list=[]
for i in range (len):
   num=random.randint(10,99)
   list.append(num)
print(*list)
list2=list[:]
for i in range (len):
    for j in range (len-1):
        if list2[j]<list2[j+1]:
            list2[j],list2[j+1]=list2[j+1],list2[j]
print(*list2)

print('Second largest Number : ',list2[1])
