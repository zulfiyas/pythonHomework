list1 = [[2, 3], 2, 4, 1, 5, 2, 4]
element = 4
replacement = 3

for i in range(len(list1)):
    if list1[i] == element:
        list1[i] = replacement  

print(list1) 