import random
l1 = []
for i in range(12):
    num = random.randint(10,99)
    l1.append(num)
 
   
   
   
print(l1)

sum1= 0
for i in range(len(l1)-9):
    sum1 = sum1+l1[i]
    min1 = l1[0]
    max1 = l1[0]
    if max1<l1[i]:
        max1 = l1[i]
   
    if min1>l1[i]:
        min1 = l1[i]
avg1 = round(sum1/3,3)
               
print("Quarter1 :",end ="")\

print(*l1[0:3],end = " ")

print("\t\tMin:",min1,"\tMAX",max1,"\t\tAverage",avg1)

sum2= 0
for i in range(3,len(l1)-6):
    sum2 = sum2+l1[i]
    min2 = l1[3]
    max2 = l1[3]
    if max2<l1[i]:
        max2 = l1[i]
   
    if min2>l1[i]:
        min2 = l1[i]
       
avg2 = round(sum2/3,3)

print("Quarter2 :",end ="")

print(*l1[3:6],end = "")

print("\t\tMin:",min2,"\tMAX",max2,"\t\tAverage",avg2)
sum3= 0
for i in range(6,len(l1)-3):
    sum3 = sum3+l1[i]
    min3 = l1[6]
    max3 = l1[6]
    if max3<l1[i]:
        max3 = l1[i]
   
    if min3>l1[i]:
        min3 = l1[i]
       
avg3 = round(sum3/3,3)

print("Quarter3 :",end ="")

print(*l1[6:9],end = " ")
print("\t\tMin:",min3,"\tMAX",max3,"\t\tAverage",avg3)

print("Quarter4 :",end ="")

sum4= 0
for i in range(9,len(l1)):
    sum4 = sum3+l1[i]
    min4 = l1[9]
    max4 = l1[9]
    if max4<l1[i]:
        max4 = l1[i]
   
    if min4>l1[i]:
        min4 = l1[i]
       
avg4 = round(sum4/3,3)
print(*l1[9:12],end = " ")
print("\t\tMin:",min4,"\tMAX",max4,"\t\tAverage",avg4)

if min1 < min2  and min1 < min3  and min1 < min4:
    print("Quarter 1 has minimum sale",min1)
if min2 < min1  and min2 < min3  and min2 < min4:
    print("Quarter 2 has minimum sale",min2)
if min3 < min1  and min3 < min2  and min3 < min4:
    print("Quarter 3 has minimum sale",min3)
if min4 < min1  and min4 < min2  and min4 < min3:
    print("Quarter 4 has minimum sale",min4)

   
if max1 > max2  and max1 > max3  and max1 > max4:
    print("Quarter 1 has maximum sale",min1)
if max2 > max1  and max2 > max3  and max2 > max4:
    print("Quarter 2 has maximum sale",min2)
if max3 > max1  and max3 > max2  and max3 > max4:
    print("Quarter 3 has maximum sale",min3)
if max4 > max1  and max4 > max2  and max4 > max3:
    print("Quarter 4 has maximum sale",max4)

if avg1 < avg2  and avg1 < avg3  and avg1 < avg4:
    print("Quarter 1 has min avg",avg1)
if avg2 < avg1  and avg2 < avg3  and avg2 < avg4:
    print("Quarter 2 has min avg",avg2)
if avg3 < avg1  and avg3 < avg2  and avg3 < avg4:
    print("Quarter 3 has min avg",avg3)
if avg4 < avg1  and avg4 < avg2  and avg4 < avg3:
    print("Quarter 4 has main avg",avg4)
   
   
if avg1 > avg2  and avg1 > avg3  and avg1 > avg4:
    print("Quarter 1 has maximum avg",avg1)
   
if avg2 > avg1  and avg2 > avg3  and avg2 > avg4:
    print("Quarter 2 has maximum avg",avg2)
if avg3 > avg1  and avg3 > avg2  and avg3 > avg4:
    print("Quarter 3 has maximum avg",avg3)
if avg4 > avg1  and avg4 > avg2  and avg4 > avg3:
    print("Quarter 4 has maximum avg",avg4)
