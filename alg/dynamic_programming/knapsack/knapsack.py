import copy
from typing import List, Tuple

# def solve(arr: List[Tuple[int, int]], cap: int) -> bool:
#     if cap == 0:
#         return True
#     if cap < 0: return False

#     for index, item in enumerate(arr):
#         weight, value = item
#         deep_copied_arr = copy.deepcopy(arr)
#         deep_copied_arr.pop(index)

#         if solve(deep_copied_arr, cap - value):
#             return True

#     return False

# def solve(arr: List[Tuple[int, int]], cap: int,weight_taken : int) -> int:
#     if cap == 0: return weight_taken
#     if cap < 0: return 0

#     best = 0

#     for index, item in enumerate(arr):
#         weight, value = item
#         deep_copied_arr = copy.deepcopy(arr)
#         deep_copied_arr.pop(index)

#         res = solve(deep_copied_arr, cap - value , weight_taken + weight)
#         best = max(res,best)

#     return best


def solve(arr: List[Tuple[int, int]], cap: int,weight_taken : int,profit : int) -> int:
    if weight_taken == cap : return profit
    
    profit = 0

    for index,(weight,value) in enumerate(arr):
        res = weight + weight_taken
        if res < cap:
            pass
    return profit


if __name__ == "__main__":
    # arr = [
    #     [1,1],  # weight and the value of it 
    #     [3,4],
    #     [4,5],
    #     [5,7]  
    # ]
    # expected = 5 # True
    # cap = 7

    arr = [
        [4,1],  # weight and the value of it 
        [5,2],
        [1,3],  
    ]
    expected = 3 
    cap = 4
    res = solve(arr,cap,0,0)
    assert res == expected ,  f"Wrong answer , expected {expected} got {res}"
    print(res)