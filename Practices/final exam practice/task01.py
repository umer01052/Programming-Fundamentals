file = open('marks.txt','r')
cout=int(file.readline())
for i in range (cout):
    roll_no=file.readline()
    m1=int(file.readline())
    m2=int(file.readline())
    m3=int(file.readline())
    m4=int(file.readline())
    avg=(m1+m2+m3+m4)/4
    if i==0:
        max_avg=min_avg=avg
        max_roll=min_roll=roll_no
    else:
        if max_avg<avg:
            max_avg=avg
            max_roll=roll_no
        elif  min_avg>avg:
            min_avg=avg
            min_roll=roll_no

file.close()
print (f'Roll No: {max_roll} has max average: {max_avg}')
print (f'Roll No: {min_roll} has min average: {min_avg}')
