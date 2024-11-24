rows=int(input('Enter ROws: '))
for i in range(rows):
    for  j in range(rows-i-1):
        print (end=' ')
    for  j in range(i+1):
        print (i-j+1, end='')
    for  j in range(i):
        print (j+2, end='')
    print()
