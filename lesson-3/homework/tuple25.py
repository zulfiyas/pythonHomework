tup = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
seen = set()
unique_ordered = []
for item in tup:
    if item not in seen:
        unique_ordered.append(item)
        seen.add(item)
print("Unique Elements:", tuple(unique_ordered))