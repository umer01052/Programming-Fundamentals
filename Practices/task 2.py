a="AI is important for its potential to change how we live, work and play. It has been effectively used in business to automate tasks done by humans, including customer service work, lead generation, fraud detection and quality control. In a number of areas, AI can perform tasks much better than humans. Particularly when it comes to repetitive, detail-oriented tasks, such as analyzing large numbers of legal documents to ensure relevant fields are filled in properly, AI tools often complete jobs quickly and with relatively few errors. Because of the massive data sets it can process, AI can also give enterprises insights into their operations they might not have been aware of. The rapidly expanding population of generative AI tools will be important in fields ranging from education and marketing to product design."   
cout=0
for i in range (len(a)):
    if a[i]==" " or a[i]=="." or a[i]==",":
        print("",end="")
    else:
        cout+=1
for i in range(65,90):
    count=0
    
    for j in range(len(a)):
        
        if a[j]==chr(i) or a[j]==chr(i+32):
            count+=1
        
    print(f'{chr(i)} appears {count} times')

print(f'TOtal Alphabets in paragrapgh:',cout)
print(f'TOtal Characters in paragrapgh:',len(a))
