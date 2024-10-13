import sys
from io import StringIO

test_input = """4
5 6
1 2 3 4 5
4 8
2 3 4 5
6 10
5 5 5 5 5 5
3 4
2 2 2
"""

sys.stdin = StringIO(test_input)



for _ in range(int(input())):
    length,target = list(map(int,input().split()))
    nums = list(map(int,input().split()))


    res = set()
    comps = {}
    for i,num in enumerate(nums):
        need = target-num
        if need in comps:
            res.add(
                (
                    min(num,nums[comps.get(need)]), #type:ignore
                    max(num,nums[comps.get(need)]) #type:ignore
                )
            )
        comps[num] = i
    if res:
        result = sorted(res)
        for r in result:
            print(r,end="")
        print()
    else:
        print(-1)


