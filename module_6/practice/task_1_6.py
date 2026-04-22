
# Задание 1
# Написать рекурсивную функцию нахождения наи
# большего общего делителя двух целых чисел.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input(''))
num2 = int(input(''))

print(f"НОД({num1}, {num2}) = {gcd(num1, num2)}") 
