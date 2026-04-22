# # генератор

# def func_1():
#     result=[]
#     for i in range(5):
#         result.append(i)
#     return result
# print(func_1())

# def func_2():
#     for i in range(5):
#         yield i
# gen = func_2()

# for i in func_2():
#     print(i)

# print(gen)
# print(next(gen))
# print(next(gen))


# рекурсия

def factorial(n):
    # базовый случай
    if n <=1:
        return 1
        # рекурсивный шаг 9! = 9*8*7*6...
    return n*factorial(n-1)
print(factorial(9))