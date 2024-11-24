rows=int(input("Enter ROws: "))
z=rows-1
b=1
for i in range (rows):
    for j in range (z):
        print(" ",end="")
    for j in range (b):
        print('*',end="")
    z=z-1
    b=b+2
    print()
