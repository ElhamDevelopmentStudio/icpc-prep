"""
given an arr of 'n' ints
find the product by multiplying 3 elements
"""

import heapq
def solve(arr: list[int]) -> int:
    """
    this fails to smth like this [-5,-2,5,1,4]
    """
    # this = heapq.nlargest(3,arr)
    # return this[0] * this[1] * this[2]
    """
    the better solution is smth like this 
    """
    sorted_arr =sorted(arr)

    normal = sorted_arr[-1] * sorted_arr[-2] * sorted_arr[-3]
    low_to_high = sorted_arr[0] * sorted_arr[1] * sorted_arr[-1]

    return max(normal,low_to_high)



if __name__ == "__main__":
    arr = [0,-1,10,7,5]
    res = solve(arr)
    print(res)