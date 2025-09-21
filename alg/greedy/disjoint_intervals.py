"""
given list of intervals [start,end]
find the length of maximal set of mutually disjoint intervals
"""

def solve(arr : list[int]) -> int:
    this = sorted(arr,key=lambda x :x[1])
    count = 0
    current_time = 0
    for start,end in this:
        if start > current_time:
            current_time = end
            count += 1
    return count

if __name__ == "__main__":
    arr = [[1,2],[2,10],[4,6]]
    res = solve(arr)
    print(res)