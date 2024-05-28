import numpy as np
def matrix_multiply(A, B):
    # Get the dimensions of the matrices
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Initialize the result matrix
    C = [[0 for _ in range(p)] for _ in range(m)]

    # Perform the matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

def multiply(a_,b_):
    c = [[operator.mul(a,b) for a in row] for b,_ in zip(a_,b_)]
    return c
f = np.array([
        [1,4],
        [3,9],
        [8,6]
        ])
l = np.array([
        [1,6],
        [2,9]
        ])

from pprint import pp
res = f @ l
print(res)
another_res = matrix_multiply(f,l)
print(another_res)
that_res = matrix_multiply(f,l)
pp(that_res)

