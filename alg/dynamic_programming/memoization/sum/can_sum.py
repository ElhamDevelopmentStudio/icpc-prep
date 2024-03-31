"""
two sum but with infinite coins
"""

"""
my first impl 
time : O(n*n)
space : O(n)
def solve(arr : list[int], target:int) -> bool:
    value = arr.pop()
    for num in arr:
        if num + value ==  target:
            return True
    return solve(arr,target)
"""

"""
better recursive impl
time : O(arr_len ^ target)
space : O(target)
def solve(arr : list[int], target:int,picks) -> bool:
    if target == 0: return True,picks
    if target < 0 : return False,picks
    for num in arr: 
        res , _ = solve(arr,target-num,f"{picks}{num}")
        if res : return True,_
    return False,None
"""

"""
memoized version
time : O(arr_len * target)
space : O(target)
"""
def solve(arr : list[int], target:int,memo : dict[int:int]) -> bool:
    if target in memo : return memo[target]
    if target == 0: return True
    if target < 0 : return False
    for num in arr: 
        memo[target] = solve(arr,target-num,memo)
        if memo[target]:
            return True
    return False

if __name__ == "__main__":
    arr = [5,3,4,7]
    target = 7
    expected = True
    # arr = [7,14]
    # target = 300
    # expected = False
    res = solve(arr,target,"")
    print(res)
    # assert  res == expected , f"Wrong answer , your answer was {res} expected {expected}"