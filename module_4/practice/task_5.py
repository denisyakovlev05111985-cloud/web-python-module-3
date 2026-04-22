def shastliv_num(num):
    if len(num)!= 6:
        return False
    elif sum(map(int, num[:3])) == sum(map(int, num[3:])):
        return True
    else:
        return False

print(shastliv_num('452254'))
print(shastliv_num('4522254'))
print(shastliv_num('452264'))