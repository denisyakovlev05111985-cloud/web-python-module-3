avto= ("BMV", "Audi", "Reno", "BMV")
izmenyem= input('')
izmenyem_na= input('')

new_avto=[]

for i in avto:
    if i == izmenyem:
        new_avto.append(izmenyem_na)
    else:
        new_avto.append(i)

new_avto_korteg = tuple(new_avto)
print(new_avto_korteg)

