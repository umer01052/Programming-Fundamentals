list1 = [10, 34, 53, 76, 89]
list2 = [24, 42, 65, 82, 120]
print(list1)
print(list2)
merge_list = [0] * 10
i = 0  
j = 0  
for k in range(10):  
    if i < 5 and j < 5:
        if list1[i] < list2[j]:
            merge_list[k] = list1[i]
            i += 1
        else:
            merge_list[k] = list2[j]
            j += 1
    else:
        merge_list[k] = list2[j]
        j += 1
print(merge_list)
