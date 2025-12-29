word= input("введите слово: ")

d= {}

for letter in word:
    d.setdefault(letter, 0)
    d[letter] +=1

for key, value in d.items():
    print(f"{key}={value}")