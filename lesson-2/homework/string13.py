a = input("Enter the string: ") 
words_list = a.split() 
cleaned_words = [word.strip() for word in words_list]  

print(cleaned_words)  
