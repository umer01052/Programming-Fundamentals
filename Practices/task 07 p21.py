rows= int(input('Enter ROws: '))
for i in range(rows):
    for j in range (i):
        print(" ",end="")
    print("\ ")
for h in range (rows):
    print(" ",end="")
for k in range (rows):
    print("-",end="")
print()
z=rows
for i in range (1,rows+1):
    for j in range (z):
        print(" ",end="")
    print("/")
    z=z-1
   
