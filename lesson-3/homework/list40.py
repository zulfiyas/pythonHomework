list1 = [1, 2, 2, 3, 4, 4, 5]

unique_list = []
for x in list1:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)