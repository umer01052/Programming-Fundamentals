rows=int(input('Enter Rows:'))
for i in range (1,rows+1):
    for j in range (1,rows-i+1):
        print(end=" ")
    print(end="*")
    for j in range (1,(i-1)*2):
        print(end=" ")
    if i>1:
        print(end="*")
    print()

for i in range(rows - 1, 0, -1):
        for j in range(rows, i, -1):
            print(end=" ")
        print(end="*")
        for j in range(1, (i - 1) * 2):
            print(end=" ")
        if i > 1:
            print (end="*")
        print()


