import random
i=1
cout=0
while i<=10:
    ch1=random.randint(0,255)
    ch2=random.randint(0,255)
    
    if ch1&1==ch2&1:
        cout+=1
    if ch1&2==ch2&2:
        cout+=1
    if ch1&4==ch2&4:
        cout+=1
    if ch1&8==ch2&8:
        cout+=1
    if ch1&16==ch2&16:
        cout+=1
    if ch1&32==ch2&32:
        cout+=1
    if ch1&64==ch2&64:
        cout+=1
    if ch1&128==ch2&128:
        cout+=1
    print(f'{chr(ch1)} and {chr(ch2)} has {cout} bit(s) same')
    i+=1
