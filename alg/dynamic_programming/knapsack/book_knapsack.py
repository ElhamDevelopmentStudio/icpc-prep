"""
from page 72 of comp prog handbook
given a list of weights , determine all sums that can be constructed 
using the weights
"""
def solve(arr : list[int]) -> list[bool]:
    pass

if __name__ == "__main__":
    arr : list[int] = [1,3,3,5]
    res = solve(arr)
    expected : list[bool] = [True, True, False, True, True, True, True, True, True, True, False, True, True]
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)