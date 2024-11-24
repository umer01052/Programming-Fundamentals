rows = int(input("Enter rows: "))
spaces = rows * 2 -2
for i in range(rows):
    for j in range(i):
        print (' ', end='')
    print("|_", end='')
    for j in range(spaces):
        print (' ', end='')
    print("_|")
    spaces = spaces - 2
