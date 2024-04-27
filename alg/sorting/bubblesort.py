def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1] , arr[j]
    return arr

arr = [-1,20,8,4,10,100,-10]
print(bubble(arr))