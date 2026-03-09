import random
n = int(input("Введите размер списка: "))
numbers = list([random.randint(-100, 100) for _ in range(n)])

print("Исходный список:", numbers)

negative_count = positive_count = zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    elif num < 0:
        negative_count += 1
    else:
        positive_count += 1

print(f"Минимальный элемент: {min(numbers)}")
print(f"Максимальный элемент: {max(numbers)}")
print(f"Количество отрицательных элементов: {negative_count}")
print(f"Количество положительных элементов: {positive_count}")
print(f"Количество нулей: {zero_count}")
