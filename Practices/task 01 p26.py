import random
len=int(input('Entr Value: '))
list=[0]*len
for i in range (len):
    list[i]=random.randint(2,99)
print(list)
for i in range (len-1):
    if list[i]<list[i+1]:
        print(list[i],list[i+1])
    else:
        print(list[i+1],list[i])
