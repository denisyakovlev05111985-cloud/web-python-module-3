# найти исполнителей у которых есть задачи in progress дольше 7 дней
# найти статусы которые встречаются только у одного исполнителя


# import random

# tasks= []

# for i in range(10):
#     tasks.append({
#         'id': i,
#         'assigne': random.choice(['ivan', 'olga', 'petr', 'anna', 'oleg']),
#         'status': random.choice(['in progress', 'blocked', 'in review', 'waiting vendor']),
#         'days in status': random.randint(0,10)
#     })
# print(tasks)

tasks= [{'id': 0, 'assigne': 'anna', 'ststus': 'in review', 'days in status': 9},
 {'id': 1, 'assigne': 'olga', 'ststus': 'in review', 'days in status': 1}, 
 {'id': 2, 'assigne': 'petr', 'ststus': 'waiting vendor', 'days in status': 6}, 
 {'id': 3, 'assigne': 'olga', 'ststus': 'waiting vendor', 'days in status': 3}, 
 {'id': 4, 'assigne': 'petr', 'ststus': 'blocked', 'days in status': 9}, 
 {'id': 5, 'assigne': 'ivan', 'ststus': 'in review', 'days in status': 6},
  {'id': 6, 'assigne': 'olga', 'ststus': 'in progress', 'days in status': 8},
   {'id': 7, 'assigne': 'anna', 'ststus': 'in progress', 'days in status': 8}, 
   {'id': 8, 'assigne': 'petr', 'ststus': 'in progress', 'days in status': 0}, 
   {'id': 9, 'assigne': 'oleg', 'ststus': 'waiting vendor', 'days in status': 10}]

in_progress= set()
for el in tasks:
    if el['ststus'] == 'in progress' and el['days in status'] > 7:
        in_progress.add(el['assigne'])

print(in_progress)

status_assigne= {}
for el in tasks:
    if el['ststus'] not in status_assigne:
        status_assigne[el['ststus']] = set()

    status_assigne[el['ststus']].add(el['assigne'])

result= {}
for ststus in status_assigne:
    if len(status_assigne[ststus]) == 1:
        result[ststus] = list(status_assigne[ststus])[0]

print(status_assigne)
print(result)

# вывести 'assigne' у которого самый большой суммарный долг по дням для 'in progress'/'blocked'

