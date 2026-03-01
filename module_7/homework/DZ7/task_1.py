logs = [
    ("ivan", 8),
    ("ivan", 10),
    ("olga", 20),
    ("petr", 45)
]

# Создаем словарь для хранения результатов
results = {}

# Проходим по каждому сотруднику
for name, hours in logs:
    # Если сотрудник уже есть в словаре, суммируем часы
    if name in results:
        results[name] += hours
    else:
        # Иначе создаем новую запись
        results[name] = hours

# Вычисляем переработки и недоработки
for name, total_hours in results.items():
    overtime = max(0, total_hours - 40)  # Переработка (если > 40 часов)
    underwork = max(0, 20 - total_hours)  # Недоработка (если < 20 часов)

    print(f"Сотрудник: {name}")
    print(f"* Общее отработанное время: {total_hours} часов")
    print(f"* Переработка: {overtime} часов")
    print(f"* Недоработка: {underwork} часов")
    print("-" * 20)