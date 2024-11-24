import random
list = [0]*20
for i in range(20):
    list[i] = list[i-1]+ random.randint(1, 20)
print("Main List :",*list)
miss=[]
for i in range (19):
    
    for i in range (list[i],list[i+1]-1):
        miss.append(i+1)
        
print("Missing :",*miss)
