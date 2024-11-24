x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
distinct_elements = []
distinct_counts = []

for element in x:
    if element not in distinct_elements:
        distinct_elements.append(element)
        distinct_counts.append(1)
    else:
        index = distinct_elements.index(element)
        distinct_counts[index] += 1

print("X:", end=" ")
for element in x:
    print(element, end=" ")
print()
print("Y:", end=" ")
for element in distinct_elements:
    print(element, end=" ")
print()
print("C:", end=" ")
for count in distinct_counts:
    print(count, end=" ")
