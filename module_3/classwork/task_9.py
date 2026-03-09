spisok = [-1, -2, -3, 1, 2, 3, 4, 5, -2, 3]

negative_count = 0
for num in spisok:
    if num < 0:
        negative_count += num
print(f"Сумма отрицательных элементов: {negative_count}")

chet_num = 0
for num in spisok:
    if num %2== 0:
        chet_num += num
print(f"Сумма четных элементов: {chet_num}")

nechet_num = 0
for num in spisok:
    if num %2!= 0:
        nechet_num += num

print(f"Сумма нечетных элементов: {nechet_num}")

ind_na_3 = 1
for num in spisok:
    if num %3== 0:
        ind_na_3 *= num
print(f"произведение чисел с индексом кратным 3: {ind_na_3}")

min_max= min(spisok)*max(spisok)
print(f"произведение мин и макс числа: {min_max}")

spisok2=[]
for num in spisok:
    if num > 0:
       spisok2.append(num)
print(spisok2)
print(sum(spisok2[1:-1]))