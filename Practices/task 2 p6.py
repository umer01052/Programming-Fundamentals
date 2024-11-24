import random
n1=random.randint(1,5)
n2=random.randint(1,5)
print('First Number: ',n1)
print('Second Number: ',n2)
if n1>n2:
    larger_num=n1
    smaller_num=n2
else:
    larger_num=n2
    smaller_num=n1
abs_difference=larger_num-smaller_num
    
if n1==n2:
    print(' Numbers are exactly equal')
elif abs_difference<=1:
    print(' Numbers are almost equal')
else:
    print(' Number are not Equal')
