tup = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
group1 = (tup[0], tup[2], tup[4]) if len(tup) >= 5 else ()
group2 = (tup[1], tup[3], tup[5]) if len(tup) >= 6 else ()
print("Nested Tuple:", (group1, group2))