import random
i=0
cout=0
sum_mid = sum_final = sum_sessional = sum_total = 0
print('Roll No\tMid\tFinal\tTotal\tGrade')
while i<=30:
    total_2=30
    mid=random.randint(0,35)
    final=random.randint(0,40)
    sessional=random.randint(0,25)
    total=mid+final+sessional
    sum_total = sum_total + total
    sum_mid = sum_mid + mid
    sum_final = sum_final + final
    sum_sessional = sum_sessional + sessional
    if total>=90:
        grade='A'
        
        cout+=1
    elif total>=80:
        grade='B'
        
        cout+=1
    elif total>=70:
        grade='C'
        
        cout+=1
    elif total>=60:
        grade='D'
        
        cout+=1
    elif total>=50:
        grade='E'
        
        cout+=1
    else:
        grade='F'
       
    i=i+1
    print(f'{i}\t{mid}\t{final}\t{total}\t{grade}')
    
total1 =cout
print('pass',total1)
fail=total_2-total1
print('fail',fail)
print ('Total: ', 30)

print ('Overall Average Marks: ', sum_total/30)
print ('Average Midterm Marks: ', sum_mid/30)
print ('Average Sessional Marks: ', sum_sessional/30)
print ('Average Final term Marks: ', sum_final/30)




    
    
    
