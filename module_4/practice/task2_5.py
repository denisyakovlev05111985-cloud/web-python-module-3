import random

nums= [random.randint(-50, 50) for _ in range(100)]

best_position=0
best_sum = None

def summa_10(i,best_position=0, best_sum=None):
    if i+10 > len(nums):
        return best_position

    summ= sum(nums[i:i+10])
    if best_sum == None or summ < best_sum:
        best_sum= summ
        best_position= i
    return summa_10(i+1, best_position, best_sum)

best_position = summa_10(0)
print(nums)
print(f"Минимальная последовательность: {nums[best_position: best_position + 10]}")
