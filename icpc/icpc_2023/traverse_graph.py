import sys
from io import StringIO
import math
input_ = """1
4 3
"""


sys.stdin = StringIO(input_)


def solve(w,h):
    n = w+h-2
    k = w-1
    return math.comb(n,k)

for _ in range(int(input())):
    cols,rows = list(map(int,input().split()))
    
    matrix = [[0] * cols for _ in range(rows)]
    matrix[0][0] = 1

    """
    0 0 0
    0 0 0
    0 0 0
    """
    for i in range(len(matrix)):
        for j in range(
           len(matrix[i]) 
        ):
            if i == 0:
                if j == 0: continue 
                matrix[i][j] = matrix[i][j-1] 
            elif j == 0:
                matrix[i][j] = matrix[i-1][j] 
            else:
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j] 


    print(
        matrix[rows-1][cols-1]
    )
    from pprint import pp
    for m in matrix: pp(m) 

