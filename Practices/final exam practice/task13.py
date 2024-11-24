def main():
    NOT_APPEARED_IN_EXAM = -2
    NOT_APPEARED_IN_PAPER = -1
    file = open('mark.txt', 'r')
    count = int(file.readline())
    count_not_appeared_in_exam = 0
    for i in range(count):
        count = 0
        rollno = int(file.readline())
        m1 = int(file.readline())
        if m1 == NOT_APPEARED_IN_EXAM:
            count_not_appeared_in_exam += 1
        else:
            m2 = int(file.readline())
            m3 = int(file.readline())
            m4 = int(file.readline())
    file.close()
    
    file = open('mark.txt', 'r')
    file_w = open('absent.txt', 'w')
    file_w.write(f'{count_not_appeared_in_exam}\n')
    
    count = int(file.readline())
    for i in range(count):
        count = 0
        rollno = int(file.readline())
        m1 = int(file.readline())
        if m1 == NOT_APPEARED_IN_EXAM:
            file_w.write(f'{rollno}\n')
        else:
            m2 = int(file.readline())
            m3 = int(file.readline())
            m4 = int(file.readline())
    file.close()
    file_w.close()

main()
