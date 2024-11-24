from random import *
def main():
	value = randint(0, 9)
	for count in range(1, 11):
		inc = randint(2, 3)
		value += inc
		print (value, end = ' ')
	print ()
	
main()
