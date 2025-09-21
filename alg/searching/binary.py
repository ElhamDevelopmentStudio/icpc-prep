from collections import deque
def find(arr,target):
    low , high = 0 , len(arr) - 1
    
    while  low <= high:
        m = (low+high) // 2

        if arr[m] == target:
            return m

        elif arr[m] > target: high = m - 1
        else: low = m +1

    
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    res = find(arr,1)
    print(res)

