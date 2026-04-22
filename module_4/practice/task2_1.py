def power(x, n):
    if n == 1:
        return x
    return x*power(x, n-1)
print(power(2, 3))