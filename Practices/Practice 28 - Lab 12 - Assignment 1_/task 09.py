import random
list=[0]*20
for i in range (20):
    list[i] = random.randint(0, 9)
print("Original list:",*list)
for i in range(2, len(list) - 2):
    average = list[i-2] + list[i-1] + list[i+1] + list[i+2]
    list[i] = average // 4
print("New list: ", *list)
