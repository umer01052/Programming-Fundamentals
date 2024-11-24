from random import *
def print_char(ch, n):
    for i in range(n):
        print(end=ch)

def main():
	rows = randint(2, 6)				#As usual I am taking random number, replace it by input statement
	print ("Rows: ", rows)
	#Print first half of the pattern
	stars_count = rows * 2
	circles_count = 0
	for i in range(1, rows+1):
		print_char('o', circles_count)
		print_char('*', stars_count)
		print_char('o', circles_count)
		print()
		stars_count -= 2
		circles_count += 1
	#Print second half of the pattern
	stars_count = 2
	circles_count -= 1
	for i in range(1, rows+1):
		print_char('o', circles_count)
		print_char('*', stars_count)
		print_char('o', circles_count)
		print()
		stars_count += 2
		circles_count -= 1

	
main()