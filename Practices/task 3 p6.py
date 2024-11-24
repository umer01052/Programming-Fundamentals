import random
n=random.randint(0,100)
if n>=85:
    grade='A'
elif n>=80:
    grade='A-'
elif n>=75:
    grade='B+'
elif n>=70:
    grade='B'
elif n>=65:
    grade='B-'
elif n>=61:
    grade='C+'
elif n>=58:
    grade='C'
elif n>=55:
    grade='C-'
elif n>=50:
    grade='D'
else:
    grade='F'
print('Marks: ',n)
print('Grade: ',grade)
