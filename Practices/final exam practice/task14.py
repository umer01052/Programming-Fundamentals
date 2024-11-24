def main():
    NOT_APPEARED_IN_EXAM = -2
    NOT_APPEARED_IN_PAPER = -1
    file = open('mark.txt', 'r')
    count = int(file.readline())
    count_not_appeared_in_all_papers = 0
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
        if count != 4:  count_not_appeared_in_all_papers += 1
    file.close()
    
    file = open('mark.txt', 'r')
    file_w = open('marks_absent.txt', 'w')
    file_w.write(f'{count_not_appeared_in_all_papers}\n')
    count = int(file.readline())
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
        if count != 4:
            file_w.write(f'{rollno}\n{m1}\n{m2}\n{m3}\n{m4}\n')
    file.close()
    file_w.close()
main()
