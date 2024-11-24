import random
Len=12
list=[0]*Len
for i in range (Len):
    list[i]=random.randint(1000,2000)
print(*list)
sum1=0
for i in range(6):
    sum1=list[i]+sum1
print(f"Sale in First half :{sum1}")
sum2=0
for i in range (6,12):
    
    sum2=list[i]+sum2

print(f"Sale in Second half :{sum2}")
for i in range(4):
        sum = 0
        for j in range(3):
            sum += list[i*3+j]
        print(f'Sale in Quarter {i+1}: {sum}')
