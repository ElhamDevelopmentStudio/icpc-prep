"""
from page 57-58 of comp prog handbook
the greedy implementation of coin_problem.py , this dosetn work effecinetly
"""



# def solve(x):
#     if x < 0 : return float("inf")
#     if x == 0 : return 0

#     best = float("inf")
#     for i in range(len(arr)):
#         best = min(best,solve(x-arr[i])+1)

#     return best


# def solve(arr : list[int],target : int) -> int:
#     d = [float("inf")] * (target + 1)
#     d[0] = 0
#     for i in range(1,target+1):
#         for c in arr:
#             if i - c >= 0:
#                 d[i] = min(d[i],1 + d[i-c])

#     return d[-1]


# res=  solve(arr,target)
# print(res)
res = []
arr = [1,2,5]
target = 5
def solve(coins, remaining):
    if remaining == 0:
        this = sorted(coins)
        if this not in res : res.append(this)
        return
    
    for coin in arr:
        if coin <= remaining:
            solve(coins + [coin], remaining - coin)

for coin in arr:
    solve([coin], target - coin)
print(res)
# for key in res:
#     print(key)
#     total = 0
#     for j in range(len(key)):
#         total += int(key[j])
#     print(f"your total is {total}")
#     assert total == target , "Wrong total buddy"
# print(res)
# print(len(res))