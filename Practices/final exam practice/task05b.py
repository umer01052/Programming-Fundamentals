import random
file=open('matrix_set1.txt','r')
file2=open("matrix_set2.txt","w")
total=int(file.readline())
file2.write(str(total)+"\n")
for i in range (total):
    rows=int(file.readline())
    cols=int(file.readline())
    file2.write(str(rows)+'\n')
    file2.write(str(cols)+'\n')
    for j in range (rows*cols):
        file.readline()
   
    for j in range (rows):
        for k in range (cols):
            value=random.randint(0,9)
            file2.write(str(value)+'\n')
file.close()
file2.close()
