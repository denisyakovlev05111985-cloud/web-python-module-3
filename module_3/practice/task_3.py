
qwe1= input('введите текст: ')
q=0
w=0
for x in qwe1:
    if x.isalpha():
        q+=1
    elif x.isdigit():
        w+=1
print(q,w)
