from io import StringIO
import sys

input_ = """1
5
8 19 3 2 0
"""

sys.stdin = StringIO(input_)

for _ in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] > nums[j]:
                count += 1

    print(count)
