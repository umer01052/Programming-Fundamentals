import random
list=[0]*10
for i in range(10):
    list[i]=random.randint(3,7)
print(*list)
for i in range (len(list)):
    for i in range (list[i]):
        print('*',end="")
    print()