x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i] == x[j]:
            x[j] = -1   # mark the duplicate element
for i in  range (len(x)):
    if x[i] != -1:
        print(x[i], end=" ")
