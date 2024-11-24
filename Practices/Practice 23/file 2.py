def print_grades(marks, limit1, limit2, limit3, limit4, limit5, g1, g2, g3, g4, g5):
    if         (marks >= limit1):    print(g1);
    elif (marks >= limit2):    print(g2);
    elif (marks >= limit3):    print(g3);
    elif (marks >= limit4):    print(g4);
    elif (marks >= limit5):    print(g5);
    else:                    print("F");

def main():
    fileg = open("grades.txt", "r")
    limit1 = int(fileg.readline())
    g1 = fileg.readline().strip()
    limit2 = int(fileg.readline())    
    g2 = fileg.readline().strip()
    limit3 = int(fileg.readline())
    g3 = fileg.readline().strip()
    limit4 = int(fileg.readline())
    g4 = fileg.readline().strip()
    limit5 = int(fileg.readline())
    g5 = fileg.readline().strip()
    rollno_in = int(input("Enter Roll No: "))
    file = open("marks.txt", "r")
    count = int(file.readline())
    for i in range(count):
        rollno_file = int(file.readline())
        m1 = int(file.readline())
        m2 = int(file.readline())
        m3 = int(file.readline())
        m4 = int(file.readline())
        if rollno_in == rollno_file:
            print ("Marks A: ", m1, end = '\t')
            print_grades(m1, limit1, limit2, limit3, limit4, limit5, g1, g2, g3, g4, g5)
            print ("Marks B: ", m2, end = '\t')
            print_grades(m2, limit1, limit2, limit3, limit4, limit5, g1, g2, g3, g4, g5)
            print ("Marks C: ", m3, end = '\t')
            print_grades(m3, limit1, limit2, limit3, limit4, limit5, g1, g2, g3, g4, g5);
            print ("Marks D: ", m4, end = '\t')
            print_grades(m4, limit1, limit2, limit3, limit4, limit5, g1, g2, g3, g4, g5);
            break
    file.close()
   
main()
