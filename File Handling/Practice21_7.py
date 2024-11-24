from random import *
def print_char(ch, n):
    for i in range(n):
        print(end=ch)

def main():
	rows = randint(3, 5)		#As usual I am taking random number, replace it by input statement
	for i in range(rows):
		print_char(' ', i)
		print('\\')     			#One \ will be ignored next will be printed
	print_char(' ', rows)
	print_char('-',rows)
	print()
	for i in range(rows, 0, -1):
		print_char(' ', i-1)
		print('/') 				#One \ will be ignored next will be printed


main()
