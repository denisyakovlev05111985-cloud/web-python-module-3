# звезды в ряд

def ryd(N):
    if N == 1:
        return '*'
    return '*' + ryd(N-1)
print(ryd(10))