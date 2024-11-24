n=int(input('Enter Value: '))
for i in range (1,n):
    temp=97
    for j in range (1,n+1):
       print(chr(temp),end=" ")
       temp=temp+i
    print()
