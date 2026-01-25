text= ('привет1 мир.привет2 мир.привет3 мир.!!')
predlog= text.split('.')
print('. '.join(x.capitalize() for x in predlog))

num=0
for x in text:
    if x.isdigit():
        num+=1
print(num)

print(len([num for x in text if x.isdigit()]))

count=0 
simbol= '!.,?;:'
for el in text:
    if el in simbol:
        count+=1
print(count)

count2=0 
simbol2= '!'
for el in text:
    if el in simbol2:
        count2+=1
print(count2)