name="Rana Umer"
first=''
second=''
for i in range (len(name)):
    if name[i]==' ':
        for j in range (i+1,len(name)):
            second=second+name[j]
        x=i
        for j in range (x) :
            first=first+name[j]
            x=x-1
print("First:",first)
print("Second:",second)
