list1 = [1, [10, 20, 30], 4, [5, 6, 7], 8, [100, 200, 300]]  
number = 2  

new_list = []  
for item in list1:  
    new_list.extend([item] * number)  

print(new_list)  