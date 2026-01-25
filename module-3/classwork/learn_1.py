# text= 'python'
# print(text[0:7])
# print(text[0:3])
# print(text[0::2])
# print(text[::-1])
# print(text[::-1])
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.swapcase())
# print(text.find('p'))
# print(text.index('t'))
# print(text.replace('pYt','654',2)) # 3 индекс количество слов под замену

# print(text.isalpha()) # проверка на буквы
# print(text.isdigit()) # проверка на цифры
# print(text.isspace()) #
# print(text.isalnum()) # буквы и цифры
# print(text.isupper()) # заглавные
# print(text.islower()) # прописные



# # очистка в строках

# text= '   cjgdjgfv   '
# print(text.strip()) # в скобках можно указать имеющийся символ для удаления 
# print(text.lstrip())
# print(text.rstrip())

# разбиение и обьединение
 
# text= 'qwe, asd, zxc'
# f= text.split(',')
# u= ','.join(f)
# print(f,u)

# text= 'qwe\nqwe\nqwe'
# sl = text.splitlines()
# print(sl)


# Кортежи

# tuple_1= (1,2,3)
# tuple_2= tuple([4,5,6])
# tuple_3= 1,2,3
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)

# tuple_4= tuple(range(0,11))
# print(tuple_4[2])
# print(tuple_4[3:6])

# num, *other, last= tuple(range(0,11))
# print(num, other, last)

# tuple1= (1, 2)
# tuple2= (3, 4)
# print(tuple1+tuple2)

# pattern = ('a', 'b')
# print(pattern * 2)

# # Принадлежность
# q= ('apple', 'banana')
# print('apple' in q)

# numbers= (1,2,3,3,2,4,5,6,2,7)
# print(numbers.count(2)) # считаем кол
# print(numbers.index(3)) # первое вхождение индекс

# num_typle= tuple(range(0,5))
# # for num in num_typle:
# #     print(num)
# for index, num in enumerate(num_typle):
#     print(index+1,num)

# tuple_sum= ('b')
# tuple_sum1= ('b',)
# print(tuple_sum,tuple_sum1)

