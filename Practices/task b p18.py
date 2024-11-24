rows=int(input('Enter Rows: '))
for i in range(rows):
    for j in range (i):
        print( "+",end=" ")
    print()
temp=rows
for i in range(rows):
    for z in range (temp):
        print( "+",end=" ")
    temp=temp-1
    print()
         



    
    

    

