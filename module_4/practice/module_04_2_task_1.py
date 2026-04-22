# Пользователь вводит с клавиатуры арифметическое 
# выражение. Например, 23+12.
# Необходимовывестинаэкранрезультатвыражения. 
# В нашем примере это 35. Арифметическое выражение 
# может состоять только из трёх частей: число, операция, 
# число. Возможные операции: +, -,*,/

primer = input('введите арифметическое выражение: ')

primer_razbiv= []
for el in primer:
    if el == '+':
        primer_razbiv = primer.split('+')
        result = sum(map(int,primer_razbiv))
    elif el == '-':
        primer_razbiv = primer.split('-')
        result= int(primer_razbiv[0])-int(primer_razbiv[1])
    elif el == '*':
        primer_razbiv = primer.split('*')
        result= int(primer_razbiv[0])*int(primer_razbiv[1])
    else:
        primer_razbiv = primer.split('/')
        result= int(primer_razbiv[0])/int(primer_razbiv[1])
print(result)



# try:
#     result = eval(primer)
#     print(result)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')