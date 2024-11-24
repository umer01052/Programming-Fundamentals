NOT_APPEARED_IN_EXAM = -2
NOT_APPEARED_IN_PAPER = -1
file = open('mark.txt', 'r')
count = int(file.readline())
count_not_appeared_in_exam = 0
for i in range(count):
    rollno = int(file.readline())
    m1 = int(file.readline())
    if m1 == NOT_APPEARED_IN_EXAM:
        count_not_appeared_in_exam += 1
        continue
        m2 = int(file.readline())
        m3 = int(file.readline())
        m4 = int(file.readline())
print(f'{count_not_appeared_in_exam} students not appeared in exam')
file.close()
