# # Операции на мноежства

# # Обьединение

# set_a= {1,2,3,4}
# set_b= {5,6,7,8}
# set_a |= set_b
# result = set_a.union(set_b)
# result_operator = set_a | set_b

# print(result, result_operator)
# print(set_a,result, result_operator)

# # Пересечение

# set_a= {1,2,3,4,6}
# set_b= {5,6,7,8,2}

# result = set_a.intersection(set_b)
# result_operator = set_a & set_b
# set_a &= set_b

# print(set_a, result, result_operator )

# # Разность

# set_a= {1,2,3,4,6}
# set_b= {5,6,7,8,2}

# result = set_a.difference(set_b)
# result_operator = set_a - set_b
# set_a -= set_b

# print(set_a, result, result_operator )

# # Симетрическая разность

# set_a= {1,2,3,4}
# set_b= {3,4,5,6}

# result = set_a.symmetric_difference(set_b)
# result_operator = set_a ^ set_b
# set_a ^= set_b

# print(set_a, result, result_operator )

# my_set= {1,2,3}
# print(3 in my_set)
# print(5 not in my_set)
# print(len(my_set))
# print(sum(my_set))
# print(max(my_set), min(my_set))

# for num in my_set:
#     print(num)