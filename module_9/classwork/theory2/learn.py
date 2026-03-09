# #1

# def devide(a,b):
#     return a/b
# print(devide(10/0))

# #2

# raw_values= ['10','5','abc','3']
# numbers= []

# for raw in raw_values:
#     try:
#         numbers.append(int(raw))
#     except ValueError:
#         print(f'Не число {raw}')
# print(numbers)

# #3

# def parse(a,b):
#     try:
#         x= int(a)
#         y= int(b)
#         return x / y
#     except ValueError:
#         return 'Ошибка a или b не число'
#     except ZeroDivisionError:
#         return 'Делить на ноль нельзя'
# print(parse('10', '2'))
# print(parse('10', '0'))
# print(parse('fbc', '2'))

# #4

# try:
#     data= {'name': 'Alise'}
#     print(data['email'])
# except KeyError as e:
#     print('Тип:', type(e).__name__)
#     print('Аргумент:', e.args)
#     print('Сообщение:', e)

# #5

# def set_discount(percent):
#     if not 0 <= percent <= 100:
#         raise ValueError('скидка должна быть в диапазоне от 0 до 100')
#     return f'скидка установлена :  {percent}'

# print(set_discount(20))
# print(set_discount(120))

# #6

# def load_user(data, user_id):
#     try:
#         return data[user_id]
#     except KeyError:
#         print(f'Пользователь не найден: {user_id}')
#         raise

# users= {1: 'Alise'}
# try:
#     print(load_user(users, 2))
# except KeyError:
#     print('Ошибка')

# #7

# class ConfigError(Exception):
#     pass

# def load_port(raw_port):
#     try:
#         return int(raw_port)
#     except ValueError as e:
#         raise ConfigError('Поле PORT должно быть целым числом')
    
# try:
#     load_port('abc')
# except ConfigError as e:
#     print('Тип:', type(e).__name__)
#     print(type(e).__cause__)

# #8

# class EmployeeError(Exception):
#     pass

# class EmployeeNotFoundError(EmployeeError):
#     massage2= 'Сотрудник не найден'

# class SalaryVaildationError(EmployeeError):
#     pass

# def find_employee(employees, emp_id):
#     if emp_id not in employees:
#         raise EmployeeNotFoundError(f'сотрудник {emp_id} не найден')
#     return employees[emp_id]

# def validate_salary(value):
#     if value < 0:
#         raise SalaryVaildationError('Зп не может быть отрицательно')
    
# try:
#     find_employee({}, 10)
# except EmployeeNotFoundError as e:
#     print(e.massage2)
# except SalaryVaildationError as e:
#     print(e)

# #9

# def normalize_percent(x):
#     assert isinstance(x, int), 'должен быть числом'
#     if not 0 <= x <= 100:
#         raise ValueError('процент должнен быть от 0 до 100')
#     return x/100

# print(normalize_percent(25))
# print(normalize_percent('abc'))