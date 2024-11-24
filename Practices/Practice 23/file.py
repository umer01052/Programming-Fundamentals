roll=int(input('Enter ROlL NO:'))
file=open('marks.txt','r')
value=int(file.readline())
miss=True
for i in range (value):
    rollno =int(file.readline())
    if rollno!=roll:
      file.readline()
      file.readline()
      file.readline()
      file.readline()
    else:
      flag=False
      print ("Marks A: ",file.readline())
      print ("Marks B: ",file.readline())
      print ("Marks C: ",file.readline())
      print ("Marks D: ",file.readline())
      break
if flag:
    print("Roll No Not Exists") 
file.close()
