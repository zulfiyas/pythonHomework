list1 = [1, [10, 20, 30], 4, [5, 6, 7], 8, [100, 200, 300]]

flattened = []
for item in list1:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)

print(flattened == sorted(flattened))
