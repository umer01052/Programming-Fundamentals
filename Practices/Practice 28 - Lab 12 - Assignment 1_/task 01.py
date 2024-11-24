import random
Len=10
list=[0]*Len
for i in range(Len):
    list[i]=random.randint(1,55)
print("Orignial list",list)
#print(*list) without brackets and commas
#reverse a list 
x=Len-1
list2=[0]*Len
for i in range (Len):
    list2[i]=list[x]
    x=x-1
print('Reverse list',list2)
