from random import *
def main():
	n1 = randint(2, 9)
	n2 = n1 + 1
	while n2 % n1 != 0:
		n2 = randint(1, 100)
	print (f'N1: {n1}\t\tN2: {n2}')

main()
