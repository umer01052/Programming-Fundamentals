file1_r = open('matrix_set1.txt', 'r')
file2_r = open('matrix_set2.txt', 'r')
file_sum = open('sum.txt', 'w')
file_diff = open('diff.txt', 'w')
num_matrices = int(file1_r.readline())
file2_r.readline()                              
file_sum.write(f'{num_matrices}\n')
file_diff.write(f'{num_matrices}\n')
for i in range(num_matrices):
        
    rows = int(file1_r.readline())
    cols = int(file1_r.readline())
    file2_r.readline();file2_r.readline();      
    file_sum.write(f'{rows}\n{cols}\n')
    file_diff.write(f'{rows}\n{cols}\n')
    for j in range(rows):
        for k in range(cols):
            value1 = int(file1_r.readline())
            value2 = int(file2_r.readline())
            file_sum.write(f'{value1 + value2}\n')
            file_diff.write(f'{value1 - value2}\n')
file1_r.close()
file2_r.close()
file_sum.close()
file_diff.close()
