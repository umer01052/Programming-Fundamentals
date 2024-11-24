from random import *

file = open("matrix.txt", "w")
rows = randint(4,8)
cols = randint(4,8)
file.write(f'{rows}\n{cols}\n')
for i in range(rows):
    for j in range(cols):
        value = randint(1, 9)
        file.write(f'{value}\n')
file.close()
	
