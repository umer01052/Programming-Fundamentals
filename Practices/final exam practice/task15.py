import random
len=10
x=[0]*len

for i in range (len):
    x[i]=random.randint(50,100)
print(*x)
sum=0
for i in range (len):
    sum=x[i]+sum
average=sum/len
print('Average : ',average)
y=[0]*len
for i in range (len):
    y[i]=x[i]-average
print(*y)

cout1=0
cout2=0
for i in range (len):
    if y[i]>0:
        cout1+=1
    else:
        
        cout2+=1
print('Count of Positive Number : ',cout1)
print('Count of Negtive Number : ',cout2)
