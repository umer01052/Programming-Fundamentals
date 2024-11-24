import random
len=int(input('Entr Value: '))
list1=[]*len
list2=[]*len
for i in range (len-1):
    list1[i]=random.randint(2,99)
    list2[i]=random.randint(2,99)
print('List 1:',list1)
print('List 2:',list2)
for i in range (len-1):
    if list1[i]>list2[i]:
        print(list1[i])
    else:
        print(list2[i])

