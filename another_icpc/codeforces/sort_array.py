import sys
from io import StringIO

input_string = """3
3 2 1
"""

sys.stdin = StringIO(input_string)

input = sys.stdin.read
data = input().strip().split("\n")

n = int(data[0])  
arr = list(map(int, data[1].split()))  

if arr == sorted(arr):
    print("yes")
    print(1, 1)
else:
    l, r = 0, n - 1

    while l < n - 1 and arr[l] <= arr[l + 1]:
        l += 1

    while r > 0 and arr[r] >= arr[r - 1]:
        r -= 1

    arr[l:r+1] = reversed(arr[l:r+1])

    if arr == sorted(arr):
        print("yes")
        print(l + 1, r + 1) 
    else:
        print("no")


