from collections import defaultdict

# Исходные данные
payments = [("ivan", 100), ("ivan", -30), ("ivan", -20), ("olga", 200), ("petr", -50)]

# Словарь для подсчёта баланса по каждому пользователю
balance = defaultdict(int)

# Словарь для подсчёта количества операций
operation_count = defaultdict(int)

# Обрабатываем каждую операцию
for user, amount in payments:
    balance[user] += amount
    operation_count[user] += 1

# 1. Баланс по каждому пользователю
print("Баланс по каждому пользователю:")
for user, bal in balance.items():
    print(f"{user}: {bal}")

# 2. Пользователи с отрицательным балансом
negative_balance_users = [user for user, bal in balance.items() if bal < 0]
print("\nПользователи с отрицательным балансом:")
print(negative_balance_users)

# 3. Пользователи с более чем 2 операциями
more_than_2_ops = [user for user, count in operation_count.items() if count > 2]
print("\nПользователи с более чем 2 операциями:")
print(more_than_2_ops)
