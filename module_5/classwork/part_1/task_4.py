logs= [
    ('ivan', 'day', 11),
    ('ivan', 'night', 1),
    ('olga','day', 6),
    ('petr', 'night', 1),
    ('anna', 'day', 1),
    ('anna', 'day', 3),
    ('anna', 'night', 3),
]

# нати сотр которые работали в разных сменах
# найти смены где суммарно меньше 8 часов
# найти сотрудников у кого больше или равно 12 часов

employee_shift= {}
shift_hours= {}
employee_hours= {}

for name, shift, hours in logs:
    if name not in employee_shift:
        employee_shift[name]= set()
    employee_shift[name].add(shift)

    if shift not in shift_hours:
        shift_hours[shift] = 0
    shift_hours[shift] += hours

    if name not in employee_hours:
        employee_hours[name] = 0
    employee_hours[name] += hours

print(employee_shift)
print(shift_hours) 
print(employee_hours)  

multiple_shift= []
for employee in employee_shift:
    if len(employee_shift[employee]) == 2:
        multiple_shift.append(employee)

shifts_less= []
for shift in shift_hours:
    if shift_hours[shift] < 8:
        shifts_less.append(shift)

employees= []
for employee in employee_hours:
    if employee_hours[employee] >=12:
        employees.append(employee)

print(multiple_shift)
print(shifts_less)
print(employees)

