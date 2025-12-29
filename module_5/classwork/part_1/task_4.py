# logs= [
#     ('ivan', 'day', 8),
#     ('ivan', 'night', 4),
#     ('olga','day', 6),
#     ('petr', 'night', 7),
#     ('anna', 'day', 4),
#     ('anna', 'day', 3),
#     ('anna', 'night', 3),
# ]
# new_logs= {}

# for el in logs:
#     name= el[0]
#     shift= el[1]
#     if name not in new_logs:
#         new_logs[name]= set()
    
#     new_logs[name].add(shift)

# for el2 in new_logs:
#     value = new_logs[el2]
#     if len(value)>1:
#         print(el2)

# new_logs_2={}

# for el in logs:
#     shift= el[1]
#     vremya= el[2]
#     if shift not in new_logs_2:
#         new_logs_2[shift]= 0
    
#     new_logs_2[shift] += vremya

# for x in new_logs_2:
#     sum_vremya= x[1]
#     if sum_vremya <= 8:
#         print()
# print(new_logs_2)
# # нати сотр которые работали в разных сменах
# # найти смены где суммарно меньше 8 часов
# # найти сотрудников у кого больше или равно 12 часов