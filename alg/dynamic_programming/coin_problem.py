"""
from page 57-58 of comp prog handbook
the greedy implementation of coin_problem.py , this dosetn work effecinetly
"""

arr = [1,5,6,9]
target = 11


def solve(x):
    if x < 0 : return float("inf")
    if x == 0 : return 0

    best = float("inf")
    for i in range(len(arr)):
        best = min(best,solve(x-arr[i])+1)

    return best

res = solve(target)
print(res)