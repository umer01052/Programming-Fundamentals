from random import *
def main():
    count = 0
    sum_values = 0
    while sum_values != 50:
        n1 = randint(0, 99)
        n2 = randint(0, 99)
        sum_values = n1 + n2
        count += 1
    print (f'N1: {n1}\t\tN2: {n2}')
    print ('Count: ', count)

main()
