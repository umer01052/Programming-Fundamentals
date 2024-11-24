from random import *
num1=randint(1,9)
num2=randint(1,9)
i=1
flag = True
chances = 2
while i<=10 and chances > 0:

    print('num1',num1)
    print('num2',num2)
    sum=num1+num2
    difference=num1-num2
    product=num1*num2
    print('sum',sum)
    print('difference',difference)
    print('product',product)
    if int(input("Enter sum: ")) != sum:
        flag= False
        
    else:
        difference=num1-num2
        product=num1*num2
        print('sum' , sum)
        print('difference' , difference)
        print('product' , product)
    if int(input('Enter Value')) != difference:
        flag = False
       
    else:
        sum=num1+num2
        product=num1*num2
        print('sum' , sum)
        print('difference' , difference)
        print('product' , product)
    if int(input('Enter Value')) != product:
        flag = False
    
    else:
        sum=num1+num2
        difference=num1-num2
        print('sum' , sum)
        print('difference' , difference)
        print('product' , product)
        
    if flag == False:
        chances -=1
        if flag == 0:
            print("Wrong ,Enter Product Again:")
        if flag==2 :
            print("Again Wrong Last Chance To Enter THe product")
    i=i+1
    
    
