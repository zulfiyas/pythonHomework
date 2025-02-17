tup = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
indices = [i for i, x in enumerate(tup) if x == 5]
print("All indices of 5:", indices)