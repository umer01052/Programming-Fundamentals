rows=int(input('Enter Value: '))
character = 65 
i = 1
while i <= rows:
    y = 1
    while y <= 4:
        print(chr(character), end=' ')
        character += 1
        y += 1
    print()
    i+=1
