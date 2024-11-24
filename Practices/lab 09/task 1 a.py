rows=int(input('Enter Rows:'))
char=65
for k in range (rows):
    for i in range (1,rows+1):
        print(chr(char),end=' ')
        for j in range(1,i+1):
             print(j, end=' ')
             
        char=char+1
    print()
