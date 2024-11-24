x = input('Enter character:')
b =int (input('Enter bit number: '))
c=b-1
d=b
n=ord (x)
if n & (2**c):
    switched = "on"
    print (f"The bit number {d} is {switched} in {x}")
else:
    switched = "off"
    print (f"The bit number {d} is {switched} in {x}")
