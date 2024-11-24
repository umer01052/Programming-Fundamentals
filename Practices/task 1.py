a="AI is important for its a potential to change how we live,work and play.It has been effectively used in business to automate tasks done by humans,including customer service work,lead generation,fraud detection and quality control.In a number of areas,AI can perform tasks much better than humans.Particularly when it comes to repetitive,detail-oriented tasks,such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly,AI tools often complete jobs quickly and with relatively few errors.Because of the massive data sets it can process,AI can also give enterprises insights into their operations they might not have been aware of.The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design."
arr=[]

for i in range (len(a)-1):
    if a[i]==" " or a[i]=="." or a[i]==',' :
        arr.append(a[i+1])
        
        
    else:
       print('',end="")

print('Word count:',len(arr))
sum=0
for i in range(65,91):
    count=0
    
    for j in range(len(arr)):
        
        if arr[j]==chr(i) or arr[j]==chr(i+32):
            count+=1
    sum=sum+count
        
    print(f'Words started from {chr(i)} are :{count} ')
print('Total words count by adding word count of individual alphabets:',sum) 
        
        
    
            

