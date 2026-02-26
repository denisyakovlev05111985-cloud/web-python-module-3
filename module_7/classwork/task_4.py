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


with open("equipment_requests.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + '\n')

with open("equipment_requests.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        date, department, employee, category = parts[0], parts[1], parts[2], parts[3]
        quantity = int(parts[4])
        status = parts[5]
    
for request in requests:
    department, employee, category, quantity, status= request[department], request[employee], request[category], request[quantity], request[status]
    
    department_stats.setdefault(department, {"total": 0, "approved": 0, "pending": 0})
    
    all_categories.add(category)
print(department_stats)
    # employee_statuses
    # TODO:
    # получить department, employee, category, quantity, status

    # 1) обновить department_stats
    # 2) добавить category в all_categories
    # 3) обновить employee_statuses
    # 4) обновить category_quantity
    