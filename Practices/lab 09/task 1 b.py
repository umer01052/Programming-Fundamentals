rows=int(input('Enter Rows:'))
spaces=rows*2
spaces2=rows*2

for i in range(rows):
    for j in range (i+1):
        print(' ',end='')
    print('*',end='')
    for j in range(spaces-1):
        print(' ',end='')
    print("*")
    spaces=spaces-2

