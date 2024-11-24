rows = int(input("Enter  rows: "))
columns = int(input("Enter  columns: "))
i = 0
while i < rows:
    y = 0
    while y < columns:
        print("*", end=" ")
        y += 1
    print(">") 
    i += 1
