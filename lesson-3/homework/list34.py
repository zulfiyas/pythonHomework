list1 = [1, 2, 3, 4, 5]
shift = 2

rotated = list1[-shift:] + list1[:-shift]
print(rotated)