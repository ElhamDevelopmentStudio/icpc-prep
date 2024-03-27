"""
given an arr of numbers 
return the number with frequency higher then
len(arr) / 2
"""

from collections import Counter
def solve(arr: list[int]) -> int:
    this_counter = Counter(arr)
    required = len(arr) / 2
    for key,value in this_counter.items():
        if value > required:
            return key
        
    """
    or 
    return Counter(arr).most_common(1)[0][0]
    """
    
if __name__ == "__main__":
    arr = [3,2,2,4,2,2]
    res = solve(arr)
    print(res)