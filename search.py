import re

def my_search():
    Path = input("Enter file path: ")
    find = input("Which word are you looking for?: ")
    
    try:
        with open(Path, 'r') as file:
            text = file.read()
        
        number_of_words = len(re.findall(find, text))
        return f"'{find}' found {number_of_words} times in the text."
    
    except FileNotFoundError:
        return "File not found. Please check the file path and try again."

print(my_search())