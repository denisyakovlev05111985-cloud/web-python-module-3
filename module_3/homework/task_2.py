
primer= input('введите матамтический пример: ')
try:
    result = eval(primer)
    print(result)
except ZeroDivisionError:
    print('На ноль делить нельзя')
