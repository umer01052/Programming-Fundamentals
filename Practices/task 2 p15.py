decimal_num = int(input('Enter Decimal Number: '))
octal_num = ''

while decimal_num > 0:
    remainder = decimal_num % 8
    octal_num = str(remainder) + octal_num
    decimal_num = decimal_num//8

print(octal_num)
