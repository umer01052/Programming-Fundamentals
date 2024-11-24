from random import *
def main():
	c1 = c2 = c3 = c4 = c5 = 'A'
	while c1 == 'A' or c1 == 'E' or c1 == 'I' or c1 == 'O' or c1 == 'U':
		c1 = chr(randint(65, 90))
	while c2 == 'A' or c2 == 'E' or c2 == 'I' or c2 == 'O' or c2 == 'U':
		c2 = chr(randint(65, 90))
	while c3 == 'A' or c3 == 'E' or c3 == 'I' or c3 == 'O' or c3 == 'U':
		c3 = chr(randint(65, 90))
	while c4 == 'A' or c4 == 'E' or c4 == 'I' or c4 == 'O' or c4 == 'U':
		c4 = chr(randint(65, 90))
	while c5 == 'A' or c5 == 'E' or c5 == 'I' or c5 == 'O' or c5 == 'U':
		c5 = chr(randint(65, 90))
	print (f'C1: {c1}\t\tC2: {c2}\t\tC3: {c3}\t\tC4: {c4}\t\tC5: {c5}')


main()
