"""
from page 77 of comp prog handbook
"""
def solve(arr : list[int] , target : int) -> bool:
    left = 0
    right = 1

    curr_sum = arr[0]
    length_of_arr = len(arr)
    while right <= length_of_arr:

        while curr_sum > target and left < right - 1:
            curr_sum = curr_sum - arr[left]
            left += 1

        if curr_sum == target:
            print(f"Sum found between indexes {left} and {right-1}")
            return True
        
        if right < length_of_arr:
            curr_sum = curr_sum + arr[right]
        right += 1
    
    return False
        
        




if __name__ == "__main__":
    arr : list[int] = [1,3,2,5,1,1,2,3]
    target : int = 8
    expected : bool = True
    res : bool = solve(arr,target)
    assert res == expected , f"Wrong answer expected {expected} got {res}"
    print(res)