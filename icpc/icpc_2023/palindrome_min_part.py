from io import StringIO
import sys

input_ ="""1
Noonabbad
"""

sys.stdin = StringIO(input_)

is_pal = lambda x : x == x[::-1] 
def solve(word,i,j):
    if i >= j or is_pal(word[i:j]):
        return 0

    best_partition = float("inf") 
    for k in range(i,j):
        left = solve(word,i,k)
        right = solve(word,k+1,j)

        this_part = left+right+1
        best_partition = min(best_partition,this_part)

    return best_partition


for _ in range(int(input())):
    word = input().lower()

    print(
        solve(
            word,
            0,
            len(word)-1
        )
    )



