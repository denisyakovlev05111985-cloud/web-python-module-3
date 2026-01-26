#сумма чисел в диапазоне

def summ(a, b):

    if a == b:
        return a
    return b + summ(a, b-1)
print(summ(1, 5))

def summ2(a, b):

    if a == b:
        return b
    return a + summ(a+1, b)
print(summ2(1, 5))