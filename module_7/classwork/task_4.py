lines = [
    "2026-02-01,IT,Иванов,Ноутбук,1,approved",
    "2026-02-01,HR,Петрова,Клавиатура,2,pending",
    "2026-02-02,Finance,Сидоров,Монитор,1,approved",
    "2026-02-02,IT,Кузнецов,Мышь,3,rejected",
    "2026-02-03,IT,Иванов,Док-станция,1,rejected",
    "2026-02-03,HR,Петрова,Гарнитура,1,approved",
    "2026-02-04,Finance,Сидоров,Клавиатура,1,pending",
    "2026-02-04,IT,Смирнов,Монитор,2,approved"
]

requests = []
# список заявок
# каждый элемент: dict с ключами
# date, department, employee, category, quantity, status

department_stats = {}
# department -> {"total": 0, "approved": 0, "pending": 0}

all_categories = set()
# множество уникальных категорий оборудования

employee_statuses = {}
# employee -> set статусов сотрудника

category_quantity = {}
# category -> суммарное количество запрошенных единиц

mixed_status_employees = []
# сотрудники, у которых есть и approved, и rejected

# Запись в файл
with open("equipment_requests.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + '\n')

# Чтение из файла и заполнение списка заявок
with open("equipment_requests.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        date, department, employee, category = parts[0], parts[1], parts[2], parts[3]
        quantity = int(parts[4])
        status = parts[5]

        # Добавляем заявку в список
        requests.append({
            'date': date,
            'department': department,
            'employee': employee,
            'category': category,
            'quantity': quantity,
            'status': status
        })

# Обработка заявок
for request in requests:
    department = request['department']
    employee = request['employee']
    category = request['category']
    quantity = request['quantity']
    status = request['status']

    # 1) Обновление статистики по отделам
    if department not in department_stats:
        department_stats[department] = {"total": 0, "approved": 0, "pending": 0}
    department_stats[department]["total"] += 1
    if status == "approved":
        department_stats[department]["approved"] += 1
    elif status == "pending":
        department_stats[department]["pending"] += 1

    # 2) Добавление категории в множество уникальных категорий
    all_categories.add(category)

    # 3) Обновление статусов сотрудников
    if employee not in employee_statuses:
        employee_statuses[employee] = set()
    employee_statuses[employee].add(status)

    # 4) Обновление суммарного количества по категориям
    if category not in category_quantity:
        category_quantity[category] = 0
    category_quantity[category] += quantity

# Поиск сотрудников с смешанными статусами
for employee, statuses in employee_statuses.items():
    if "approved" in statuses and "rejected" in statuses:
        mixed_status_employees.append(employee)

# Поиск самой востребованной категории
top_category = None
top_quantity = 0
for category, total_quantity in category_quantity.items():
    if total_quantity > top_quantity:
        top_quantity = total_quantity
        top_category = category

# Запись отчёта в файл
with open("equipment_report.txt", "w", encoding="utf-8") as file:
    file.write("Статистика по отделам:\n")
    for department, stats in department_stats.items():
        file.write(f"{department}: всего заявок — {stats['total']}, одобрено — {stats['approved']}, в ожидании — {stats['pending']}\n")

    file.write("\nСписок уникальных категорий оборудования:\n")
    for category in sorted(all_categories):
        file.write(f"- {category}\n")

    file.write("\nСотрудники с заявками разных статусов (approved и rejected):\n")
    if mixed_status_employees:
        for employee in sorted(mixed_status_employees):
            file.write(f"- {employee}\n")
    else:
        file.write("Нет сотрудников с заявками разных статусов.\n")

    file.write(f"\nСамая востребованная категория оборудования: {top_category} ({top_quantity} единиц)\n")


