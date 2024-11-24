from random import *
def main():
    sum1 = 0
    while sum1 != 50:
        value = randint(1, 10)
        sum1 += value
        print (value, end = ' ')
        if sum1 > 50:
            print ()
            sum1 = 0
    print ()

main()
