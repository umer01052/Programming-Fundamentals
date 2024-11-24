rows = int (input('Entr Rows: '))

for i in range (1,rows+1):
    for j in range (1,rows-i+1):
        print(end=" ")
    for j in range (1,i+1):
        print(i+j-1,end="")
    for j in range (i,1,-1):
        print(i+j-2,end="")
    print()
