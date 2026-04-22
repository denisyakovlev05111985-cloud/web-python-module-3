nambers = (1, 23, 456, 2, 34, 345, 4, 5, 67, 1234)
count={}
for el in nambers:
    nambers_len= len(str(abs(el)))

    if nambers_len in count:
        count[nambers_len] +=1
    else:
        count[nambers_len] =1

for count, n in count.items():
    print(count, n)

