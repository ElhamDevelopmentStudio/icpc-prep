"""
https://stackoverflow.com/questions/48098179/what-is-the-logic-to-use-bitwise-operation-in-generating-subsequences

time : O(n*(2**n))

it basically does this
| 5 | 7 | 8 | 9 |    Sequence
-----------------    --------
| 1 | 0 | 0 | 0 | -> 5
| 1 | 1 | 0 | 0 | -> 5 7
| 1 | 0 | 1 | 0 | -> 5 8
"""


def main(arr, n):
    for i in range(0, 1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)

arr = [1, 2, 3]
n = len(arr)
main(arr, n)
