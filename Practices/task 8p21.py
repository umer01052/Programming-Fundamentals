r=int(input('Enter Rows:'))
c=int(input('Enter columns:'))
spaces=c
spaces2=c-2
for i in range (r-1):
    if i==0:
        for j in range (c):
            print('o',end="")
        for j in range (c):
            print(' ',end="")
        for j in range (c):
            print('o',end="")
        print()
    else:
        for j in range (spaces):
            print(' ',end="")
        print("o",end="")
        for j in range (spaces2):
            print(' ',end="")
        print('o',end="")
        for j in range (spaces):
            print(' ',end="")
        print()
        spaces=spaces+1
        spaces2=spaces2-1
spaces3=c+1
spaces4=c-3
for i in range (r):
    if i==r-1:
        for j in range (c):
            print('o',end="")
        for j in range (c):
            print(' ',end="")
        for j in range (c):
            print('o',end="")
        print()
    else:
        for j in range (spaces3):
            print(' ',end="")
        print("o",end="")
        for j in range (spaces4):
            print(' ',end="")
        print('o',end="")
        for j in range (spaces3):
            print(' ',end="")
        print()
        spaces3=spaces3-1
        spaces4=spaces4+1
        
    
