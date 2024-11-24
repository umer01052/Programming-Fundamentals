x=ord(input('Enter CHarcter 1: ' ))
y=ord(input('Enter CHarcter 2: ' ))
cout=0
if x&1==y&1:
    cout=cout+1
if x&2==y&2:
   cout=cout+1
if x&4==y&4:
   cout=cout+1
if x&8==y&8:
    cout=cout+1
if x&16==y&16:
    cout=cout+1
if x&32==y&32:
   cout=cout+1
if x&64==y&64:
    cout=cout+1
if x&128==y&128:
    cout=cout+1
print(f'{chr(x)} and {chr(y)} has {cout} bit(s) are same')
