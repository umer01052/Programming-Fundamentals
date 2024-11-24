from random import *

def print_char(ch, times):
	for i in range(times):
		print (end=ch)
#part a(1)
def print_box(rows, columns):
	#We have first and last same line and second to second last are same
	#I am creating another function for my help, pr _chars
	print_char('*', columns)	#First line of the box
	print()     				#Move to next line
	for i in range(rows-2):		#Loop to pr  middle lines of the box
		print(end='*')
		print_char(' ', columns-2)	#There are two stars at the boundary and there are columns - 2 spaces
		print('*')
	print_char('*', columns)	#Last line of the box
	print()	        			#Move to next line

#part b(1)
def print_k_multiples_of_n(n, k):
    for i in range(1, k+1):
        print (n * i, end = ' ')
    print ()

#part c(1)
def print_n_random_values(a, b, n):
    for i in range(n):
        value = randint(a, b)
        print (value, end = ' ')
    print ()
#part d(1)
def print_quadratic_roots(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        print ('Roots are imaginary')
        return
    disc_sq = disc ** 0.5
    x1 = (-b + disc_sq) / (2 * a)
    x2 = (-b - disc_sq) / (2 * a)
    print (f'X1: {x1}', end = '\t')
    print ('X2: ', x2)

def main():
	#Driver code to check the function
	#print_box(3,5)
	#print()
	#print_box(6,8)
    #print_k_multiples_of_n(2, 6)
    #print()
    #print_k_multiples_of_n(5, 4)
    #print_n_random_values(20, 60, 5)
    #print()
    #print_n_random_values(10, 80, 5)
    print_quadratic_roots(-2, 2, 1)
    print()
    print_quadratic_roots(3, 5, 2)

main()
