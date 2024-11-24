import random
marks = []
for i in range(30):
    num = random.randint(0,100)
    marks.append(num)
print(*marks)
roll = []
for i in range(1,31):
    roll.append(i)

stud_removed = random.randint(3,5)
for i in range(stud_removed):
    roll[random.randint(0, len(roll))] = -1
print(roll)
print("Roll No\t       Marks")
for i in range(len(roll)):
    if roll[i] != -1:
        print(f"{roll[i]}\t\t{marks[i]}")
num_remaining_students    = 0  
for i in range(len(roll)):
    if roll[i] != -1:
        num_remaining_students = num_remaining_students+1
               
remaining_roll = []
remaining_marks = []
for i in range(len(roll)):
    if roll[i] != -1:
        remaining_roll.append(roll[i])
        remaining_marks.append(marks[i])
print(remaining_roll)
print(remaining_marks)

