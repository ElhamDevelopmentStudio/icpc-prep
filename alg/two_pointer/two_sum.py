"""
from page 78 of comp prog handbook
"""

"""
leet code solution
def solve(arr : list[int] , target:int) -> list[int,int]:
    indexes  : dict[int:int] = {x:i for i,x in enumerate(arr)}
    print(indexes)
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        this_res = arr[left]+arr[right]
        if this_res == target:
            print(f"here with {arr[left]} and {arr[right]} ")
            return [indexes[arr[left]],indexes[arr[right]]]
        if this_res < target:
            left += 1
        elif this_res > target:
            right -= 1
    return -1
"""





if __name__ == "__main__":
    # arr  = [4,5,9,1,7,9,10,6]
    # target = 12
    arr = [3,2,4]
    target = 6
    expected = True
    res = solve(arr,target)
    assert res == expected , f"Wrong answer , expected {expected} got {res}"
    print(res)