from random import *
def main():
	n1 = randint(1, 10)
	n2 = n3 = n1
	while n2 == n1:
		n2 = randint(1, 10)
	while n3 == n1 or n3 == n1:
		n3 = randint(1, 10)
	print (f'N1: {n1}\tN2: {n2}\t\tN3: {n3}')


main()
