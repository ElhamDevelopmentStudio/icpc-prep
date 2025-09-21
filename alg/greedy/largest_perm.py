"""
given an arrry A of a random  permutation of numbers from 1 to N.
Given B , the number of swaps in A we can make.
find the largest perm possible
"""
from collections import deque
def solve(arr : list[int] ,num_of_swaps : int) -> list[int]:
    this = deque(sorted(arr))
    d = {x:i for i,x in enumerate(arr)}
    for i in range(num_of_swaps):
        this_max_value = this.pop()
        if arr[i] != this_max_value :
            temp_a = d[arr[i]] # index of first value 
            temp_b = d[this_max_value] # index of the max value
            d[this_max_value] = temp_a
            d[arr[i]] = temp_b
            arr[i],arr[temp_b] = this_max_value,arr[i] # swap them here

    
    return arr
if __name__ == "__main__":
    # A = [3,2,4,1,5]
    # B = 3
    A = [1,2,3,4]
    B = 1
    res = solve(A,B)
    print(res)