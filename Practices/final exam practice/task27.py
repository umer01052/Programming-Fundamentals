import random

# Create a 2D list of size 4x4
matrix = [[0 for _ in range(4)] for _ in range(4)]

# Initialize elements with random two-digit numbers
for i in range(4):
    for j in range(4):
        matrix[i][j] = random.randint(10, 99)

# Print elements in a single line
for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=" ")
print()

# Print the principal diagonal
for i in range(4):
    print(matrix[i][i], end=" ")
print()

# Print the secondary diagonal
for i in range(4):
    print(matrix[i][3 - i], end=" ")
print()
