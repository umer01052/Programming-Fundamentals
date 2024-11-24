import random
file1 = open('matrix_set1.txt', 'r')
file2 = open('matrix_set2.txt', 'w')
d=int(file1.readline())
file2.write(str(d)+"\n")
for k in range (d):
    rows = int(file1.readline())
    columns = int(file1.readline())
    for i in range (rows*columns):
        file1.readline()

    file2.write(str(rows)+'\n')
    file2.write(str(columns)+'\n')

    for i in range(rows):
        for j in range(columns):
            g=random.randint(0,9)
            file2.write(str(g)+'\n')
            
file1.close()
file2.close()

