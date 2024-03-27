"""
this is the way to solve this probelm not the last implementation
""
"""

def solve(arr : list[list[int,int]]) -> int:
    times = []
    for i in arr:
        times.append((i[0],+1))
        times.append((i[1],-1))

    times.sort(key = lambda x : x[0])
    curr = 0
    max = 0

    for i in times:
        curr += i[1]
        if curr > max : max = curr
    return max


if __name__ == "__main__":
    intervals = [
        [0,2],
        [4,6],
        [0,4],
        [7,8],
        [9,11],
        [3,10]
    ]
    res = solve(intervals)
    print(res)