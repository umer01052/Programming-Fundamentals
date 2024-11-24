import random
sum=0
while sum!=50:
    num=random.randint(1,10)
    sum=num+sum
    print(num,end=" ")
    if sum>50:
        sum=0

print("\nSum=",sum)
