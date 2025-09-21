import sys
from io import StringIO

test_input = """4
1
5
2
1 1
3
1 2 3
4
2 1 2 2
"""
sys.stdin = StringIO(test_input)


for _ in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    if len(nums) == 1:
        print(1)
    else:
        res = [True] * length
        
        for i,num in enumerate(nums):
            if i == 0:
                if num == nums[i+1] and res[i+1] == True:
                    res[i] = False
            elif i == len(nums) - 1:
                if num == nums[i-1] and res[i-1] == True:
                    res[i] = False
            else:
                if num == nums[i+1] and res[i+1] == True:
                    res[i] = False
                if num == nums[i-1] and res[i-1] == True:
                    res[i] = False
        count = 0
        for r in res:
            if r : count += 1
        print(count)


