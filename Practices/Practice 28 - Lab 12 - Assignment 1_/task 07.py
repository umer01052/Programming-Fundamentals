import random
list = [0]*10
for i in range(10):
    list[i] = random.randint(1, 5)
print(list)
for i in range (10):
    
    for j in range (i+1,10):
        if list[i]==list[j]:
            
            print(f"Element {list[i]} appears at position {i} and {j}")
            
