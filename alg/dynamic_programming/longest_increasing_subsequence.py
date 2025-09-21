"""
from page 71 of comp prog handbook
"""

# O(n^2) since there is 2 nested loops
def solve(arr : list[int]) -> int:
    table = [1] * len(arr)
    for k in range(len(arr)):
        for i in range(k):
            if arr[i] < arr[k]:
                # if this index of i is smaller then get all of the subsequences of it and add + 1 to it 
                # since the new value of k is also counting
                table[k] = max(table[k],table[i]+1)
    return max(table)


if __name__ == "__main__":
    arr : list[int] = [6,2,5,1,7,4,8,3]
    res : int =  solve(arr)
    expected : int = 4
    assert res == expected , f"Wrong answer , expected {expected} got {res}"
    print(res)
