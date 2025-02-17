list1 = [1, 2, 3, 4, 5, 6, 7, 8]
size = 3

nested_list = [list1[i:i+size] for i in range(0, len(list1), size)]
print(nested_list)