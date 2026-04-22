fruct = input('введите название фрукта: ')
fructs= (
    'яблоко',
    'банан',
    'апельсин',
    'яблоко'
)
    
qwe=0

for el in fructs:
    if fruct in el:
        qwe+=1

print(qwe)