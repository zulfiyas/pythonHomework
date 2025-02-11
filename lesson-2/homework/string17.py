vowels = "aouieAOUIE" 
string = input("Enter the string: ")
new_string = "".join(char for char in string if char not in vowels)
print("Modified string:", new_string)