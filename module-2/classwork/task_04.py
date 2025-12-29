text= "Hello World"
replacements= {"e": 1, "l": 2, "o": 3, "r": 4}
result = ""
for char in text:
    result += str(replacements.get(char, char))
print(result)