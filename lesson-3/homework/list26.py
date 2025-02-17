list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(list1)

if length % 2 == 0:  
    middle_element = [list1[length // 2 - 1], list1[length // 2]]
else:  
    middle_element = list1[length // 2]  

print(middle_element)  