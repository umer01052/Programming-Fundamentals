import random
len=int(input('Enter Value: '))
x=[0]*len
for i in range (len):
    x[i]=random.randint(50,100)
print('X=',x)
y=x[:]
print('Y=',y)
SEN=-1
for i in range (len):
    cout=0
    if x[i]!=SEN:
        for j in range(len):
            if x[i]==x[j]:
                cout+=1
                x[i]=SEN
        print(f'{y[i]} has count{cout}')
