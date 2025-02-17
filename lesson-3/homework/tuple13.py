tup = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
unique = set(tup)
if len(unique) < 2:
    print("Second Smallest: None")
else:
    sorted_unique = sorted(unique)
    print("Second Smallest:", sorted_unique[1])