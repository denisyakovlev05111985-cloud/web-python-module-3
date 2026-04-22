def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
print(bubble_sort([5,2,-5,1,0]))
print(bubble_sort([34,2,-5,1,0,-23]))