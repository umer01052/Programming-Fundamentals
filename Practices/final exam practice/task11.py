NOT_APPEARED_IN_EXAM = -2
NOT_APPEARED_IN_PAPER = -1
file = open('mark.txt', 'r')
count = int(file.readline())
count_appeared_in_all_papers = 0
for i in range(count):
    count = 0
    rollno = int(file.readline())
    m1 = int(file.readline())
    if m1 == NOT_APPEARED_IN_EXAM:
        continue
    elif m1 != NOT_APPEARED_IN_PAPER:   count += 1;
    m2 = int(file.readline())
    if m2 != NOT_APPEARED_IN_PAPER:   count += 1;
    m3 = int(file.readline())
    if m3 != NOT_APPEARED_IN_PAPER:   count += 1;
    m4 = int(file.readline())
    if m4 != NOT_APPEARED_IN_PAPER:   count += 1;
    if count == 4:  count_appeared_in_all_papers += 1
print (f'{count_appeared_in_all_papers} students appeared in all papers')
