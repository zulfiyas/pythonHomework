list1 = [1, 2, 3, 2, 4, 2, 5]
element = 2

indices = [i for i, x in enumerate(list1) if x == element]
print(indices)
