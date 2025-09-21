"""
from page 238 of comp prog handbook

given n heaps , anybody who removes the last stick wins

"""

def optimal_sol(heaps : list[int] , xor_res : int) -> int:
    for sticks in heaps:
        if sticks & xor_res: return sticks
    return heaps[0]

def nim_sum(heap : list[int]) -> bool:
    res = 0
    for sticks in heap: res ^= sticks
    return res



def solve(n : int) -> bool:
    return nim_sum(n)


if __name__ == "__main__":
    n = [10,12,5] 
    res = solve(n)
    if res != 0: print(True)
    else: print(False)
