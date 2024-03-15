def count_sort(arr):
    count_arr = [0 for i in range(len(arr)+1)]
    for i in range(len(arr)):
        count_arr[arr[i]-1] += 1

    res = []
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
                 res.append(i+1)
    print(res)
    return res