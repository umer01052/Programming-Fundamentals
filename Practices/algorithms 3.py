rows=int(input('Enter ROws:'))

for i in range (1,rows+1):
    for j in range(1, rows - i + 1):
        print(end=" ")
    print(end="*")
    for j in range(1, ( i - 1 ) * 2):
        print(end=" ")
    if i > 1:
        print(end="*")
    print()
