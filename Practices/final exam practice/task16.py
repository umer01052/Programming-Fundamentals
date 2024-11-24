from random import *
def main():
    length = 30
    marks = [0] * length
    pass_count = 0
    sum = 0
    for i in range(length):
        marks[i] = randint(0, 100)
        if marks[i] >= 50:  pass_count += 1;    sum += marks[i];
        print (marks[i], end = ' ')
    average = sum / pass_count
    print (f'\nAverage of pass students: {average:0.2f}')
    positive_count = negative_count = 0
    print ('Marks of fail students:')
    for i in range(length):
        if marks[i] < 50: print (marks[i], end = ' ');
    print ('\nMarks of above average students:')
    for i in range(length):
        if marks[i] > average: print (marks[i], end = ' ');
    print ('\nMarks of below average students:')
    for i in range(length):
        if marks[i] >= 50 and marks[i] < average: print (marks[i], end = ' ');
    print()
    
main()
