vowels = ["a", "o", "u", "i", "e"]
a = input("Enter the string: ")
b = sum(a.count(vowel) for vowel in vowels)
c = len(a) - b

print("Sum of vowels: ", b)
print("Sum of consonants: ", c)