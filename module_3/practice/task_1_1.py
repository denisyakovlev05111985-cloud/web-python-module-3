qwe=[1,25,3,45,1]
qwe1=[1,2,36,45]

qwe2=qwe+qwe1
print(qwe2) # элементы обоих списков

qwer= list(set(qwe2))
print(qwer) # элементы обоих списков без повторений;

qwer1= list(set(qwe) & set(qwe1))
print(qwer1) # общие для двух списков

qwer= list(set(qwe2))
print(qwer) # уникальные элементы обоих списков без повторений;

qwer2= max(max(qwe),max(qwe1))
qwer3= min(min(qwe),min(qwe1))
print(qwer2, qwer3) # минимальное и максимальное значение из списков