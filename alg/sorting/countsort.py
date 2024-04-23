def count_sort(arr):
    count_arr = [0 for i in range(len(arr)+1)]
    for i in range(len(arr)):
        count_arr[arr[i]-1] += 1

    res = []
    print(count_arr)
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
                 res.append(i+1)
    print(res)
    return res


if __name__ == "__main__":
    arr = [1,10,4,5,9]
    res = count_sort(arr)
    print(res)