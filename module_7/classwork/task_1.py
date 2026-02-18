"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""

with open('inventory.txt', 'w', encoding='utf-8') as file:
      file.write('2024-01-01,яблоко,IN,50\n')
      file.write('2024-01-02,банан,IN,30\n')
      file.write('2024-01-03,яблоко,OUT,10\n')
      file.write('2024-01-03,груша,OUT,5\n')
      file.write('2024-01-04,груша,IN,20\n')
      file.write('2024-01-05,банан,OUT,40\n')
      file.write('2024-01-06,яблоко,OUT,5')

operations=[]
with open('inventory.txt', 'r', encoding='utf-8') as file:
   for line in file:
      date, product, operation_type, quantity= line.strip().split(',')
      operations.append({
         'date': date,
         'product': product,
         'operation_type': operation_type,
         'quantity': int(quantity)
      })

total= {}
ins={}
outs={}

for operation in operations:
   date, product, operation_type, quantity= operation['date'], operation['product'], operation['operation_type'], operation['quantity']

   total.setdefault(product, 0)
   ins.setdefault(product, 0)
   outs.setdefault(product, 0)
   
   if 'IN' == operation_type:
      total[product] += quantity
      ins[product] += quantity
   
   else:
      total[product] -= quantity
      outs[product] += quantity

for key, value in total.items():
   print(f':на складе {key}: {value}')

for key, value in ins.items():
   print(f':приехало {key}: {value}')

for key, value in outs.items():
   print(f':отгружено {key}: {value}')
