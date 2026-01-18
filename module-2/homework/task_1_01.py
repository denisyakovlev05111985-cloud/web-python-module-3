# print("hjbugugy")
# print(5,"jhfyfyf")
# print("jhsdjhsjh: ", 1,  34 , 56, sep="", end="!!!!!")
# print("\"jhsdjhsjh: ", 1,  34 , 56, sep="|")

# print(10*10)
# print(10**3)

# print(min(4,6,78,2,5,-7))
# print(max(4,6,78,2,5,-7))
# print(abs(-7))
# print(pow(5,3))
# print(round(5/3))

# input("введите: ")

# number= 5
# print(number)
# number += 2
# print("результат:",number)

# digit= 4.5437535
# word= 'Heloo'

# boolean= True

# str_num= '5'

# print(word + str(digit))
# print(digit + int(str_num))
# print(word + str(digit + int(str_num)))

# print(word, boolean)

# a1= int(input( 'введите число1: '))
# a2= int(input( 'введите число2: '))
# print('result: ', a1 + a2)

# word= 'Hi'
# print(word*3)

# if 5 > 5:
#     print("yes")

# user_data= int(input("введите число: "))

# isHappy = True

# if isHappy or user_data == 6:
#     print("good")
# elif user_data == 5:
#     print("true")
# else:
#     print("no")

# if user_data != 5:
#     print("yes")
#     if user_data > 6:
#         print('hi')

# data = input()

# number = 5 if data == "five" else 0

# if data == "five":
#     number = 5
# else:
#     number = 0

# print(number)

# for i in range(1,8,2):
#     print(i)

# count = 0
# word = 'Hello World!'
# for i in word:
#     if i == 'l':
#         count += 1
# print("кол-во символов:", count )

# i = 5

# isHasCar = True

# while isHasCar:
#     if input('enter data ') == 'stop':
#         isHasCar = False


    # print(i)
    # i += 2

# for i in range(1, 11):
#     if i ==5:
#         break

#     if i % 2 == 0:
#         continue

#     print(i)

# found = None
# str = 'hello'
# for i in str:
#     if i == "й":
#         found = True
#         break
# else:
#     found = False
# print(found)

# nums = [5,67,-67,567, True, 'Hello', 6.8779,[3,8,90]]
# nums[0]= 50
# nums[4]= 56.09
# print(nums[-1][1])
# print(nums[7])
# print(nums[5])
# print(nums)

# numbers = [5,2,7]
# # numbers[3]= 100
# numbers.append(100)
# numbers.insert(1, True)
# numbers.extend([5,6,8])
# numbers.sort()
# numbers.reverse()
# numbers.pop()
# numbers.remove(100)
# numbers.pop(0)
# print(numbers)
# print(numbers.count(5))
# print(len(numbers))

# nums= [5,2,7,'50', False]

# print(nums)
# for el in nums:
#     el *= 2
#     print(el)

# n= int(input('введите длину списка: '))
# user_list= []
# i= 0
# while i < n:
#     string= 'enter el №'+ str(i+1)+ ': '
#     user_list.append(input(string))
#     i += 1
# print(user_list)

# word = 'it- Pr- og- er'

# hobby= word.split('- ')
# for i in range(len(hobby)):
#     hobby[i] = hobby[i].capitalize()

# result= '...'.join(hobby)

# print(word[1])
# print(len(word))
# print(word.count('i'))
# print(word.upper())
# print(word.isupper())
# print(word.islower())
# print(word.lower())
# print(word.capitalize())
# print(word.find('r'))
# print(word.split('-'))
# print(hobby[1])
# print(hobby)
# print(result)

# word = 'Football'
# print(word[0:4])
# print(word[4:])
# print(word[1:-1])
# print(word[1:-1:2])

# lis= [6,4,'str', True, 6.5]
# print(lis[2])
# print(lis[2:])
# print(lis[2:-1])
# print(lis[::2])
# print(lis[::-1])

# q= int(input('='))
# w= int(input('='))
# e= int(input('='))

# print(q*100+w*10+e)
# print(q+w+e)

# q= 100 # стоимость 1кг картошки
# w= 20 # кол-во необходимое купить в кг
# name= 'картофель'

# print(f'{name} {w} кг стоит {q*w} руб')

# q, w, e = input().split() # периметр треугольника с дробными значением сторон
# q= float(q)
# w= float(w)
# e= float(e)

# print(q+w+e)

# q= int(input('проверка на четность: '))

# if q%2 == 0:
#     print('число четное')
# else:
#     print('нечетное')

# q= int(input('остаток средств на карте? '))
# price= int(input('стоимость костюма? '))
# if q >= price:
#     print('покупаю')
#     q -= price
# else:
#     print('не достаточно средств')
# print(f'{q} руб остаток средств на карте')

# q= int(input('введите год'))
# if q%4 == 0 and q%100 != 0 or q%400 == 0:
#     print('високосный')
# else:
#     print('не високосный')

# q= int(input())
# w= int(input())

# # if q>=w:
# #     print(q)
# # else:
# #     print(w) 

# print(q if q>=w else w)

# q= 0
# w= int(input('ввести число сумму чисел до которого посчитать '))
# summ= 0

# while q<=w:
#     summ+= q
#     q+= 1
# print(summ)

# q= int(input('ввести число от 1 до 9 '))

# # w= 0
# # while w<10:
# #     w+= 1
# #     print(f'{q} * {w} = {q*w}')
   
# for i in range(1,11,3):
#     print(f'{q} * {i} = {q*i}')

# st= '  Gfdgfd hgghfgf   '
# st= st.strip().upper() # стрип уберает пробелы в начале и в конце
#                        # аппер переводит все содержимое в верхний регистр
# print(st)

# a1= '13674897'
# a2= '2986h8798'
# # print('число' if a1.isdigit() else 'не число' )
# # print('число' if a2.isdigit() else 'не число' )
# if a1.isdigit():
#     print(f'{a1} число')
# else:
#     print(f'{a1} не число')
# if a2.isdigit():
#     print(f'{a2} число')
# else:
#     print(f'{a2} не число')

# # for i in a1:
# #     if i not in '0123456789':
# #         print('не число')
# #         break
# # else:
# #     print('число')
# # for i in a2:
# #     if i not in '0123456789':
# #         print('не число')
# #         break
# # else:
# #     print('число')


# text = 'hjzgxhjxg jkbxjhbx jcxhhjxcsh Hi hjbhbjhb Hi Hi Hi !!!'
# index = text.find('Hi') # с какого индекса начинается слово Hi
# print(f'первое вхождение слова Hi начинается с индекса: {index}')
# new_text1= text.replace('Hi',"Bingo") # замена исходного текста
# new_text2= text.replace('h','QEW!!!')
# print(new_text1)
# print(new_text2)

# word= ['програм-ие ','на ','питоне ','круть']
# st= ''.join(word) + '!' # объединить слова в предложение
# print(st)

# a = '  привет мой друг, учимся программировать  '
# qo = a.strip().count(' ') # считаем кол-во слов,
#                           # сперва убераем лишние пробелы
# print(qo+1)

# q= input('слово для проверки - ')

# print('палиндром' if q==q[::-1] else 'не палиндром')

# # if q == q[::-1]:
# #     print('палиндром')
# # else:
# #     print('не палиндром')

# q= int(input())
# w= int(input())

# for i in range(q, w+1, 1):
#     print(i)

# q= int(input('ввести число и посчитать сумму всех чисел в диапазоне до него '))
# summ= 0
# for i in range(0,q+1):
#     summ+= i
# print(summ)

# a= int(input())
# b= int(input())

# for i in range(a):
#     if i == b:
#         print('число в диапазоне')
#         break
# else:
#     print('число не найдено')

# q= [1,2,2,3,4,5,5,5,6,9]
# w= set(q)
# print(len(w))
# print(w)
# print(list(w))

# q= [1,2,3,4,5]  # вывести общие элементы
# w= [3,4,5,6,7]

# e= set(q)
# r= set(w)

# print(list(e & r))

# text= 'qwe asd qwe asd zxc asd zxc' # удалить повторки
# w= text.split()
# q= set(w)
# print(' '.join(q))

# q= list(map(int,input().split()))

# # print(sum(q))

# w= 0
# for i in q:
#     w+= i
# print(w)

q= [ 1 , 3, 5 , 67]
# q= list(map(int,input().split()))
print(max(q))
print(min(q))

# q= [1, 1, 2, 3, 3, 4, 5, 5, 5]
# w= set(q)
# print(w)

# q= list(map(int,input().split()))
# # w= list(set(q))
# w=[]
# for i in q:
#     if i not in w:
#         w.append(i)

# print(w)

# q= [ 1, 2, 3, 44, 55, 6]
# w= []
# for i in q:
#     if i%2==0 not in w:
#         w.append(i)
# print(w)

# n= 6
# w= []
# for i in range(n):
#     q= []
#     for j in range(n):
#         value= (i + j)%2
#         q.append(value)
#     w.append(q)
# for q in w:
#     print(*q)
    
# q = [[1, 2, 5],[6, 45, 57],[4, 45, 9]]
# m_sum = sum(q[0])
# m_ind = 0
# for i in range(0,len(q)):
#     r_sum = sum(q[i])
#     if r_sum> m_sum:
#         m_sum = r_sum
#         m_ind = i+1
# print(m_ind,m_sum)

# n = 7
# tr= []
# for i in range(n):
#     qwe = [1] * (i+1)
#     for j in range(1,i):
#         qwe[j] = tr[i-1][j-1] + tr[i-1][j]
#     tr.append(qwe)
# for qwe in tr:
#     print(*qwe)

# q= [
#     [10, 5, 8],
#     [2, 3, 7],
#     [3, 6, 5, 8]
# ]
# count = 0
# for i in q:
#     for j in i:
#         if j%2==0:
#             count+= 1
# print(count)

# product= {
#     'молоко': 'напиток',
#     'мясо': 'еда',
#     'сок': 'напиток',
#     'хлеб': 'еда',
#     'кепка': 'одежда',
# }
# qwe= {}

# for i,j in product.items():
#     if j not in qwe:
#         qwe[j]= []
#     qwe[j].append(i)
# print(qwe)

# q= {'a': 2, 's': 3,'d': 1}
# w= {'s': 4,'d': 2, 'f': 5}
# qw = q.copy()
# for key, value in w.items():
#     qw[key] = qw.get(key,0) + value
# print(qw)

# s= input()
# w= 'aeiouAEIOU'
# q=0
# for i in s:
#     if i in w:
#         q+=1
# print(q)

# q= int(input('ввести число и посчитать сумму чисел '))
# w=0
# summ=0
# for i in range(q+1):
#     if w<=q:
#         summ += w
#         w += 1
    
# print(summ)

# w= int(input('ввести число сумму чисел до которого посчитать '))
# summ= 0

# while q<=w:
#     summ+= q
#     q+= 1
# print(summ)

# q= int(input('проверка четности'))
# print('четное'if q%2==0 else 'не четное')

# qwe= 'привет, Мир!'
# for i in range(1,10+1):
#     print(qwe)

# q= int(input('конечное число списка '))#шаг 5
# for i in range(1,q+1,5):
#     print(i)

# q= 1
# while q<=50:
#     print(q)
#     q+=5

# spisok= []
# # numbers= [1,3,6,9,12]
# # print(numbers)
# numbers= [1,3,6,9,12,2.45, True, 'qwe',[1,3,6,9,12]]
# print(numbers)

# prim1= ['jehdgeud','kksdjdh','cmdoojkp']
# # print(prim1[-1])
# # for i in prim1:
# #     print(i)
# prim1.append('hhyuyg')
# print(prim1)
# prim1.pop()
# print(prim1)

# q= prim1.index('cmdoojkp')
# print(q)

# print(len(prim1))

# numbers= [1, 3, 6, 56, 78, 43]
# numbers.sort()
# print(numbers)

