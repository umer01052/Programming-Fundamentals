first=str(input('Enter  first Value:'))
second=str(input('Enter second Value:'))
third='' 

for j in range (len(first)):
    third=third+first[j]
third=third+'.'
for j in range (len(second)):
    third=third+second[j]
print(third)
