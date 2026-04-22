"""
ЗАДАЧА: Умный контроль доступа (бейджи)

Даны записи содержащие журнал проходов сотрудников.

Каждая строка файла имеет формат:
дата,имя,действие

Где:
- дата     — строка в формате YYYY-MM-DD
- имя      — имя человека
- действие — ENTER (вход) или EXIT (выход)

Журнал проходов:
2026-02-01,Иван,ENTER
2026-02-01,Мария,ENTER
2026-02-01,Иван,EXIT
2026-02-01,Иван,EXIT
2026-02-01,Олег,EXIT
2026-02-02,Мария,EXIT
2026-02-02,Олег,ENTER

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать проходы в файл access.log

2. Прочитать файл access.log и загрузить данные.

3. Для каждого человека:
   - посчитать количество входов (ENTER)
   - посчитать количество выходов (EXIT)
   - определить, находится ли человек ВНУТРИ в конце лога
     (ENTER без последующего EXIT)

4. Найти людей с ошибками доступа:
   - EXIT без предварительного ENTER
   - два ENTER подряд без EXIT
   (сохранить таких людей в множество)

5. Для каждой даты посчитать количество входов (ENTER).

6. Найти дату с максимальным количеством входов.

7. Записать подробный отчёт в файл access_report.txt.
"""
log = [
    "2026-02-01,Иван,ENTER",
    "2026-02-01,Мария,ENTER",
    "2026-02-01,Иван,EXIT",
    "2026-02-01,Иван,EXIT",
    "2026-02-01,Олег,EXIT",
    "2026-02-02,Мария,EXIT"
]

with open('access.log', 'w', encoding='utf-8') as file:
   file.write('2026-02-01,Иван,ENTER\n')
   file.write('2026-02-01,Мария,ENTER\n')
   file.write('2026-02-01,Иван,EXIT\n')
   file.write('2026-02-01,Иван,EXIT\n')
   file.write('2026-02-01,Олег,EXIT\n')
   file.write('2026-02-02,Мария,EXIT')

operations=[]

with open('access.log', 'r', encoding='utf-8') as file:
   for line in file:
      date, name, action= line.strip().split(',')
      operations.append({
         'date': date,
         'name': name,
         'action': action
      })
      print(date, name, action)

total_action_enter={}
total_action_exit={}
inside={}
errors= set()
daily_enters={}

for operation in operations:
   date, name, action= operation['date'], operation['name'], operation['action']

   total_action_enter.setdefault(name, 0)
   total_action_exit.setdefault(name, 0)
   inside.setdefault(name, False)
   daily_enters.setdefault(date, 0)
   
   if 'ENTER' == action:
      total_action_enter[name] += 1
   else:
      total_action_exit[name] +=1

   if 'ENTER' == action:
      if inside[name]:
         errors.add(name)
      inside[name] = True
      daily_enters[date] += 1
   else:
      if not inside[name]:
         errors.add(name)
      inside[name]= False

   max_day= None
   max_enters= 0
   for date, count in daily_enters.items():
      if count > max_enters:
         max_day = date
         max_enters = count



for key, value in inside.items():
   print(f' {key}: {value}') 

for key, value in total_action_enter.items():
   print(f'входов {key}: {value}')     

for key, value in total_action_exit.items():
   print(f'выходов {key}: {value}')

print(f'люди с ошибками доступа {errors}')
print(f'датa {max_day} с максимальным количеством входов {max_enters}')


with open('access_report.txt', 'w', encoding='utf-8') as file:
   file.write('количество входов\n')
   for key, value in total_action_enter.items():
      file.write(f' {key}: {value}\n')
   file.write('количество выходов\n')
   for key, value in total_action_exit.items():
      file.write(f' {key}: {value}\n')
   file.write('находится ли человек ВНУТРИ... Да- True. Нет- False\n')
   for key, value in inside.items():
      file.write(f' {key}: {value}\n')
   file.write(f'люди с ошибками доступа {errors}\n')
   file.write(f'датa {max_day} с максимальным количеством входов {max_enters}\n')
   
