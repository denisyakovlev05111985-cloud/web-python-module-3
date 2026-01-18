# qwe=[1, 2, 3, True]
# qwe1=[1, 2, 3, True, [3, 4]]
# print(qwe)
# print(len(qwe)) # длина списка
# print(len(qwe1))

# qwe2=[1, 3, 45, 67]
# print(sum(qwe2))

# qwe3= [1, 34, 56, 7]
# print(max(qwe3))
# print(min(qwe3))

# qwe4= [23, 4, 56, 7]
# print(sorted(qwe4))
# print(sorted(qwe4, reverse= True)) # список в обратном порядке

# qwe5= [23, 4, 56, 7]
# print(list(reversed(qwe5))) # list переводит список в читабельный вид

# qwe6= ['apple', 'cherry', 'banana']
# for index, fruсt in enumerate(qwe6):
#     print(f"{index+1}:{fruсt}")

# qwe5= [23, 4, 56, 7]
# s= list(map(lambda x: x**2, qwe5)) 
# print(s)

# qwe5= ['23', '4', '56', '7']
# s= list(map(int, qwe5)) 
# print(s)

# def double(num):
#     return num*2
# print(list(map(double, s)) )

# numbers= [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x: x%2 == 0, numbers)))
# def ff(num):
#     return num%2==0
# print(list(filter(ff, numbers)))

# words = ['paper','apple','car']
# res= "-".join(words)
# print(res)


# words = ['paper',2,'apple','car']
# words.append(444)
# words.extend([5,78])
# print(words)

# words = ['paper',2,'apple','car']
# words1 = ['paper',345,'apple','car']
# new = words + words1
# words+=words1
# print(new, words)

# words = ['paper',2,'apple','car']
# words.insert(1, True)
# words.insert(3, 'car')
# print(words)
# words.remove('car')
# print(words)
# words.pop()
# words.pop(1)
# print(words)
# words.clear()
# print(words)

# qwe= [2,2,4,56,7,88,88,88,97]
# res= qwe.count(88)
# print(qwe.reverse())
# qwe.sort()
# print(qwe)
# qwe.sort(reverse= True)
# print(res)
# print(qwe)



# qwe= [2,2,4,56,7,88,88,88,97]
# print(qwe[0:5])
# print(qwe[0:5:2])
# print(qwe[:6])
# print(qwe[3:])
# print(qwe[:])  # копируем
# print(qwe[-2])
# print(qwe[-2:])
# print(qwe[::-1])


# qwe1= [1,2,3,4,5,6,7,8,9,10]
# res= [x**2 for x in qwe1]
# res2=[]
# for x in qwe1:
#     res2.append(x**2)
# print(res,res2)

# qwe1= [1,2,3,4,5,6,7,8,9,10]
# res= [x for x in qwe1 if x%2==0]

# print(res)

# qwe1= [1,2,3,-4,5,6,7,8,9,10]
# res= [0 if x<0 else x for x in qwe1]

# print(res)


# word= ['apple','banana','car', 'gdgfddf','cgf']
# res= [x for x in word if len(x)>=4]
# print(res)

# numbers= [0,1,2,3,4,5,6,7,8,9]
# n= int(input('введите число: '))
# print(numbers[::n])

# numbers= [0,1,2,3,4,5,6,7,8,9,10]
# srd= sum(numbers)/len(numbers)
# print(srd)
# res=list([x for x in numbers if x>srd])
# print(res)
