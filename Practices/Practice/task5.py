x =int(input('Enter Value : '))
if x%2==0 and x%3==0 and x%5==0 and x%7==0:
    print('number is divisible by 2 and 3 and 5and 7')
elif x%2==0 and x%3==0 and x%5==0:
    print('number is divisible by 2 and 3 and 5 ')
elif x%3==0 and x%5==0 and x%7==0:
    print('number is divisible by 3 and 5 and 7')
elif(x%2==0) and x%5==0 and x%7==0 :
    print('number is divisible by 2 and 5 and 7 ')
elif(x%2==0)and x%3==0:
    print('number is divisible by2 and 3 ')
elif(x%2==0)and x%5==0:
    print('number is divisible by2 and 5 ')
elif(x%2==0)and x%7==0:
    print('number is divisible by2 and 7 ')
elif(x%3==0)and x%5==0:
    print('number is divisible by 3 and 5 ')
elif(x%3==0)and x%7==0:
    print('number is divisible by3 and 7 ')
elif(x%5==0)and x%7==0:
    print('number is divisible by5 and 7 ')
elif(x%2==0):
    print('number is divisible by 2 only ')
elif(x%3==0):
    print('number is divisible by 3 only ')
elif(x%5==0):
    print('number is divisible by 5 only')
elif(x%7==0):
    print('number is divisible by 7 only')

