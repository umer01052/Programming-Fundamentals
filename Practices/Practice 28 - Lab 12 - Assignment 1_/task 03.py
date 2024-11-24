import random
Len = 10
list1 = [0] * Len
for i in range(len(list1)):
    list1[i] = random.randint(1,55)
print('Original list: ', list1)
list2 = [list1[i] for i in range(len(list1))]
print("New list: ", list2)
#list2=list1[:] another simple way to copy a list
