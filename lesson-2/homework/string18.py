string = input("Enter a string: ").strip()
words = string.split()
if words[0] != words[-1]:
    print("Yea, it starts with one word and ends with another")
else:
    print("No, it starts with one word and ends with the same one")
