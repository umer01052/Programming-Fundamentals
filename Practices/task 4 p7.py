n1=int(input('ENter Number 1: '))
n2=int(input('ENter Number 2: '))

if n1>=85:
    grade1='A'
elif n1>=80:
    grade1='A-'
elif n1>=75:
    grade1='B+'
elif n1>=70:
    grade1='B'
elif n1>=65:
    grade1='B-'
elif n1>=61:
    grade1='C+'
elif n1>=58:
    grade1='C'
elif n1>=55:
    grade1='C-'
elif n1>=50:
    grade1='D'
else:
    grade1='F'
if n2>=85:
    grade2='A'
elif n2>=80:
    grade2='A-'
elif n2>=75:
    grade2='B+'
elif n2>=70:
    grade2='B'
elif n2>=65:
    grade2='B-'
elif n2>=61:
    grade2='C+'
elif n2>=58:
    grade2='C'
elif n2>=55:
    grade2='C-'
elif n2>=50:
    grade2='D'
else:
    grade2='F'
print('First Number:',n1)
print('Second Number:',n2)
if n1==n2:
    print('Same')
elif grade1==grade2:
    print('Almost Same')
else:
    print('Different')
