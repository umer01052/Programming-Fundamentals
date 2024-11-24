rows= int(input('Enter Value: '))

for i in range(1,rows+1):
    temp=65
    for j in range(1,rows+1):
        print(chr(temp),end=" ")
        temp=temp+i
    print()
    value=1
    for j in range(1,rows+1):
        print(value,end=" ")
        value=value+i
    print()
    

