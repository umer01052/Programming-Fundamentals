from random import *
def print_char(ch, n):
    for i in range(n):
        print(end=ch)

def main():
	rows = randint(2, 6)            #As usual I am taking random number, replace it by input statement
	if rows % 2 == 0:	rows+=1;	#rows should be odd for the pattern
	columns = randint(3, 5)
	print ("Rows: ", rows)
	print ("Columns: ", columns)
	#handle first and last line separately and middle of the lines separately
	print_char('o', columns)
	print_char(' ', rows)
	print_char('o', columns)
	print()
	spaces1 = columns
	spaces2 = rows - 2
	for i in range(1, rows, 2):
		print_char(' ', spaces1)
		print(end='o')
		print_char(' ', spaces2)
		print("o")
		spaces1 += 1
		spaces2 -= 2
	#Print middle line
	print_char(' ', spaces1)
	print("o")
	spaces1 -= 1
	spaces2 = 1
	for i in range(1, rows, 2):
		print_char(' ', spaces1)
		print(end="o")
		print_char(' ', spaces2)
		print("o")
		spaces1 -= 1
		spaces2 += 2
	#print last line
	print_char('o', columns)
	print_char(' ', rows)
	print_char('o', columns)
	print()


main()
