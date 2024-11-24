import random
file=open('matrix_set1.txt','w')
file.write(str(10)+"\n")
for i in range (10):
   rows=random.randint(2,6)
   columns=random.randint(2,6)
   file.write(str(rows)+"\n")
   file.write(str(columns)+"\n")
   for i in range (rows):
      for j in range (columns):
          c=random.randint(0,9)
          file.write(str(c)+"\n")
file.close()
