rows=int(input('Enter rows: '))
columns=int(input('Enter columns: '))
for i in range (1,rows+1):
    sum = 0
    temp=1
    for j in range (1,columns):
        print(temp,end="+")
        sum = sum + temp
        temp=temp+i
    print(temp,end=' ')
    sum=sum+temp
    
    temp=temp+i
    print('=',end=' ')
    print(sum)
    
