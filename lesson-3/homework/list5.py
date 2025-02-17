list1 = [1, 2, 3, 4, 5]
element = int(input("Enter an element you want to check for an existance: "))
if element in list1:
    print(f"{element} is in the list")
else:
    print(f"{element} is not in the list")