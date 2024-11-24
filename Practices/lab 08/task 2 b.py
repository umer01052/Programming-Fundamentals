rows = int(input("Enter the  rows: "))
columns = int(input("Enter the  columns: "))
i = 1
while i <= rows:
    y = 1
    while y <= columns:
        print('*', end=' ')
        y += 1
    print()
    i += 1
