row=int(input('Enter Value: '))
n=row
j=1
for i in range (row):
    for i in range (n):
        print(end="+")
    for i in range (j-1):
        print(end=" ")
    for i in range (j-1):
        print(end=" ")
    for i in range (n):
        print("+",end="")
    j=j+1
    n=n-1
    print()
j=1
x=row-1
for i in range(x):
    for i in range (j+1):
        print(end="+")
    for i in range (x-1):
        print(end=" ")
    for i in range (x-1):
        print(end=" ")
    for i in range (j+1):
        print("+",end="")
    j=j+1
    x=x-1
    print()
