import random
cout=0
sum=0
while sum!=50:
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    sum=num1+num2
    if sum!=50:
        cout=cout+1
print(cout)
    
    
