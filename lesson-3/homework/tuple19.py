tup = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
lst = list(tup)
if 1 in lst:
    lst.remove(1)
print("Tuple after removing 1:", tuple(lst))