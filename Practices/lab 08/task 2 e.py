rows=int(input('Enter Rows:'))
i = 1
while i <= rows:
    count = 0
    j = 1
    while j <= i+4:
        count += j
        print(j, end=' ')
        j += 1
    
    print('= ' + str(count), end=" ")
    print()
    i+=1
    
