import random
list = []
for i in range(10):
    num = random.randint(1, 15)
    while num in list:  
        num = random.randint(1, 15)
    list.append(num)

print(list)
