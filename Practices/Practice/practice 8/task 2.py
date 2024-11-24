x=input('Enter first character')
y=input('Enter second character')
a=ord(x)
b=ord(y)
print(a,b)
samebits=0
if a & (2**0) == b &(2**0):
     samebits=samebits+1
if a&(2**1)== b&(2**1):
     samebits=samebits+1
if a&(2**2)== b&(2**2):
     samebits=samebits+1
if a&(2**3)== b&(2**3):
     samebits=samebits+1
if a&(2**4)== b&(2**4):
     samebits=samebits+1
if a&(2**5)== b&(2**5):
     samebits=samebits+1
if a&(2**6)== b&(2**6):
     samebits=samebits+1
if a&(2**7)== b&(2**7):
     samebits=samebits+1
print(f'In {x} and {y},{samebits} bits are same')
     
