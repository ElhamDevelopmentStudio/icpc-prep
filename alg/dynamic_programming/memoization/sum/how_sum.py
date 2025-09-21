"""
returns the arr of how it got there
"""
from typing import Optional

"""
time : O(n^m * m)
space : O(m)
def solve(arr : list[int], target:int) -> Optional[list[int]]:
    if target == 0 : return []
    if target < 0 : return None

    for num in arr:
        res = solve(arr,target-num)
        if res != None:
            res.append(num)
            return res
    return None
"""

"""
memoized version here
time : O(n*m^2)
space : O(m^2)
"""
def solve(arr : list[int], target:int,memo:dict[int,int]) -> Optional[list[int]]:
    if target in memo : return memo[target]
    if target == 0 : return []
    if target < 0 : return None

    for num in arr:
        res = solve(arr,target-num,memo)
        if res != None:
            memo[target] = res + [num]
            return memo[target]
    memo[target] = None
    return None


if __name__ == "__main__":
    arr = [5,3,4,7]
    target = 7
    res = solve(arr,target,{})
    print(res)