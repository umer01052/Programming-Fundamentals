rows = int(input('Enter ROWs: '))
z=rows*2
for i in range (rows):
    for j in range (i):
        print("o",end="")
    for j in range(z):
        print('*',end="")
    for j in range (i):
        print("o",end="")
    z=z-2
    print()
y=rows-1
k=2
for i in range (rows):
    for j in range (y):
        print("o",end="")
    for j in range(k):
        print('*',end="")
    for j in range (y):
        print("o",end="")
    y=y-1
    k=k+2
    print()
        
        
