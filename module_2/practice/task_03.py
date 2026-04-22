prices= {"bread": 20, "milk": 80, "cheese": 25}
cart= {"bread": 2, "cola": 1, "cheese": 3}

total=0

for key, value in cart.items():
    if key in prices:
        total += prices.get(key) * value
    else:
        print("цена на данный товар отсутствует")
print(total)

