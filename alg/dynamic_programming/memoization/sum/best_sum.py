"""
coin problem
"""
from typing import Optional
"""

def solve(arr : list[int], target:int) -> Optional[list[int]]:
    if target == 0 : return []
    if target < 0 : return None

    shortest = None
    for num in arr:
        ans = solve(arr,target-num)
        if ans != None:
            result = ans + [num]
            if shortest == None or len(result) < len(shortest):
                shortest = result

    return shortest
"""

def solve(arr : list[int], target:int,memo:dict[int,int]) -> Optional[list[int]]:
    if target in memo : return memo[target]
    if target == 0 : return []
    if target < 0 : return None

    shortest = None


    for num in arr:
        ans = solve(arr,target-num,memo)
        if ans != None:
            result = ans + [num]
            if shortest == None or len(result) < len(shortest):
                shortest = result

    memo[target] = shortest
    return shortest


if __name__ == "__main__":
    # arr = [2,3,5]
    # target = 8
    # expected = [5,3]
    arr = [1,2,5,25]
    target = 100
    expected = [25,25,25,25]
    res = solve(arr,target,{})
    assert res == expected , f"Wrong answer , your answer was {res} expected {expected}"
    print(res)