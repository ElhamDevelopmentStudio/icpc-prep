"""
'...x...x'
find the minimal steps for them to take to reach each other
in here it is 2
'..x..x..x'
in here it will be 4
"""

"""
O(n^2) implementation
-----------------------
def solve(arr : str) -> int:
    crosses = [i for i,c in enumerate(arr) if c == "x"]
    crosses = [(cross - i) for i,cross in enumerate(crosses)]

    n = len(crosses)
    if n== 0 : return 0
    ans = float('inf')

    for segment_start in range(len(arr)):
        total = 0
        for cross in crosses:
            total += abs(cross - segment_start)
            
        ans = min(ans,total)
    return ans
"""




"""
def solve(arr : str) -> int:
    ..x..x.x..x.
    ....xxxx...
    # O(n) but not correct , this was my first impl
    indexes_of_people  = [i for i,x in enumerate(arr) if x =="x"]
    middle = indexes_of_people[len(indexes_of_people) // 2]
    print(f"middle is {middle}")
    print(f"indexes is {indexes_of_people}")
    diff = 0
    for key in indexes_of_people:

        if key == middle : continue
        elif key + 1 == middle or key-1 == middle : continue
        else:
            diff += abs(key-middle) - 1
    return diff
"""


def solve(arr : str) -> int:
    crosses = [i for i,c in enumerate(arr) if c == "x"]
    
    crosses = [(cross - i) for i,cross in enumerate(crosses)]
    n = len(crosses)
    if n== 0 : return 0
    ans = float('inf')

    segment_start = crosses[n // 2]
    total = 0
    for cross in crosses:
        total += abs(cross - segment_start)
        
    ans = min(ans,total)
    return ans



if __name__ == "__main__":
    this = "....x..xx..xx.."
    res = solve(this)
    print(res)
