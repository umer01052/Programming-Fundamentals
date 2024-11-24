from random import *
def main():
    file_new = open("marks_classes.txt", "w")
    for j in range(5):          
        count = randint(7,10)
        file_new.write(str(count)+'\n') 
        for i in range(1, count+1):
            file_new.write(str(i)+'\n')
            detail = f'{randint(1, 100)} {randint(1, 100)} {randint(1, 100)} {randint(1, 100)}\n'
            file_new.write(detail)
    file_new.close()
	
main()
