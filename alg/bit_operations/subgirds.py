"""
form page 101 of comp prog handbook
"""

# def solve(arr : list[list[int]],n : int) -> int:
#     subgrids = 0
#     for a in range(n):
#         for b in range(a+1,n):
#             count = 0
#             for i in range(n):
#                 if arr[a][i] == 1 and arr[b][i] == 1: count += 1
#             subgrids += ((count - 1) * count) // 2
#     return subgrids

def solve(arr : list[list[int]],n : int) -> int:
    subgrids = 0
    for a in range(n):
        for b in range(a+1,n):
            row_a = int("".join([str(x) for x in arr[a]]),2) 
            row_b = int("".join([str(x) for x in arr[b]]),2) 
            count = (row_a&row_b).bit_count()
            subgrids += ((count - 1) * count) // 2
    return subgrids




if __name__ == "__main__":
    # arr : list[list[int]] = [
    #     [0,1,0,0,1],
    #     [0,1,1,0,0],
    #     [1,0,0,0,0],
    #     [0,1,1,0,1],
    #     [0,0,0,0,0],
    # ]
    arr : list[list[int]] = [
        [1, 1 ,1 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0],
        [1, 1 ,1 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0],
    ]
    res : int = solve(arr,len(arr))
    assert res == 2 , f"got {res}"
    print(res)