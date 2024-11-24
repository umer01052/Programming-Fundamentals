rows=int(input('Enter Rows: '))
temp=rows
for i in range (rows-1):
    for j in range (i):
        print(' ',end=" ")
    
    for k in range (temp):
        print("+",end=" ")
    temp=temp-1
    print()
temp=rows-1
for s in range(rows):
    for n in range(temp):
        print(' ',end=" ")
    temp=temp-1

    for t in range (s+1):
        print( "+",end=" ")
    print()
   
