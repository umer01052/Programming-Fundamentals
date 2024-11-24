import random
len=10
list=[0]*len
for i in range (len):
    list[i]=random.randint(10,99)
print(*list)
list_copy=list[:]
for i in range (len):
    for j in range (len-1):
        if list_copy[j] > list_copy[j + 1]:
            list_copy[j], list_copy[j + 1] = list_copy[j + 1], list_copy[j]
    print(*list_copy)
print('---------------------------------------')
SEN=-1
for i in range (len):
    num=list[i]
    if list_copy!=SEN:
        index=0
        for j in range (len):
            if num==list_copy[j]:
                index=j
                SEN=list_copy[j]
   
        print(f'{num} is at position {index}')
  
    
        

    



    
