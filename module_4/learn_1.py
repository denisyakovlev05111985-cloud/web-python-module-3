# def func_1():
#     print('функция')
# func_1()

# def func_2():
#     return 'qwe qwe'
# print(func_2())

# def func_3():
#     pass    # для пропуска 

# def func_4(name, age, city):
#     print(f'{name}-{age}-{city}')
# func_4('Den', '40', 'Новочебоксарск')
# func_4(
#     name= 'Den',
#     age= '40',
#     city= 'Новочебоксарск'
# )

# def func_6(*args):   # позиционные параметры
#     total=0
#     for num in args:
#         total+= num
#     print(total)
# func_6(1,2,3,4,5)

# def func_7(**kwargs):  # именованые параметры
#     print(kwargs)
# func_7(name=1, age=2)

# def func_8(num1, num2, *args, **kwargs):
#     print(f'{num1},{num2}')
#     print(args)
#     print(kwargs)
# func_8(1, 2, 3, 4, 5, name=1)

# def func_9(obj):
#     print(obj)
    
# func_9({'a': 1, 'b': 2})

def nechet_num(num1, num2):
    for num in range(num1, num2):
        if num%2 != 0:
            print(num)
nechet_num(5, 10)