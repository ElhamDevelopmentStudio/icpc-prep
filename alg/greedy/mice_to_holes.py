"""
given 'n' mices and 'N' holes . 
a mice takes 1 minute to travel 1 unit left or right 
find the minimum time after which all mice are in holes
    -----------------
    # mice = [3,2,-4]
    # hole = [0,-2,4]
              3 -> 4 -> 1
              2 -> 0 -> 2
              -4 -> -2 -> 2      
"""


"""
my naive O(n^2) impl
which dosent even work
def solve(mices : list[int],holes: list[int]) -> int:
    res = []
    for mice in mices:
        this_mice_min = float("inf")
        this_mice_hole_index = None
        for index,hole in enumerate(holes):
            if this_mice_min > abs(mice-hole):
                this_mice_hole_index = index
                this_mice_min = abs(mice-hole)
        holes.pop(this_mice_hole_index)
        res.append(this_mice_min)
    print(holes)
    print(res)
    return max(res)
"""
def solve(mices : list[int],holes: list[int]) -> int:
    mices.sort()
    holes.sort()

    res = []
    for index,mice in enumerate(mices):
        res.append(abs(mice-holes[index]))
    return max(res)


if __name__ == "__main__":
    # mice = [3,2,-4]
    # hole = [0,-2,4]
    mice = [ -49, 58, 72, -78, 9, 65, -42, -3 ]
    hole = [ 30, -13, -70, 58, -34, 79, -36, 27 ]
    res = solve(mice,hole)
    print(res)
    # assert res == 2 , "Wrong answer"