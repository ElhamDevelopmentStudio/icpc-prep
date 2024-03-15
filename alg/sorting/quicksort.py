def quicksort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr.pop()
    less = [arr[i] for i in range(len(arr)) if arr[i] < pivot]
    great = [arr[i] for i in range(len(arr)) if arr[i] > pivot]
    return quicksort(great) + [pivot] + quicksort(less)