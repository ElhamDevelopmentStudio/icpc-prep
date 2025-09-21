"""
from page 57-58 of comp prog handbook
the greedy implementation of coin_problem.py , this dosetn work effecinetly
"""

import heapq

arr = [1,5,6,9]
heapq._heapify_max(arr)
target = 11

res = []

while target > sum(res):
    at = 0
    while at <= len(arr):
        if sum(res) + arr[at] <= target:
            res.append(arr[at])
            at = 0
            break
        else:
            at += 1


print(res)