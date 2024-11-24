def main():
    NOT_APPEARED_IN_EXAM = -2
    NOT_APPEARED_IN_PAPER = -1
    file = open('mark.txt', 'r')
    no_of_students = int(file.readline())
    rollno = int(input('Enter Roll No:'))
    if rollno < 1 or rollno > no_of_students:
        print('Roll No is out of range')
        return                              
    for i in range(no_of_students):
        sum = 0                                 
        count = 0                              
        rollno_in_file = int(file.readline())
        m1 = int(file.readline())
        if m1 == NOT_APPEARED_IN_EXAM and rollno == rollno_in_file:
            print ('Student has not appeared in the exam')
            break                                           
        elif m1 == NOT_APPEARED_IN_EXAM:    continue;       
        if rollno != rollno_in_file:    m2 = int(file.readline()); m3 = int(file.readline()); m4 = int(file.readline());
        else:
            if m1 != NOT_APPEARED_IN_PAPER: sum += m1;  count += 1;     print(f'Subject 1: {m1}');
            else:                                                       print('Absent in Subject 1')
            m2 = int(file.readline())
            if m2 != NOT_APPEARED_IN_PAPER: sum += m2;  count += 1;     print(f'Subject 2: {m2}');
            else:                                                       print('Absent in Subject 2')
            m3 = int(file.readline())
            if m3 != NOT_APPEARED_IN_PAPER: sum += m3;  count += 1;     print(f'Subject 3: {m3}');
            else:                                                       print('Absent in Subject 3')
            m4 = int(file.readline())
            if m4 != NOT_APPEARED_IN_PAPER: sum += m4;  count += 1;     print(f'Subject 4: {m4}');
            else:                                                       print('Absent in Subject 4')
            average = sum / count
            print(f'Average: {average}')
            break  
    file.close()

main()
