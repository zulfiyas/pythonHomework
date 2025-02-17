list1 = [1, [10, 20, 30], 4, [5, 6, 7], 8, [100, 200, 300]]

sublist_index = 3  

if isinstance(list1[sublist_index], list):
    print("Min of sublist:", min(list1[sublist_index]))
else:
    print("Selected element is not a sublist.")