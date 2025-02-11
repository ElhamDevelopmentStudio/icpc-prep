import sys
from io import StringIO


input_string = """5
3
6 6 6
3
6 9 12
3
12 9 6
6
2 3 5 7 11 13
8
2 3 5 7 11 13 17 19
"""


def is_fabulosa(ladder):
    len_ladder = len(ladder)
    if len_ladder:
        # wtf happens if there is only 1 ladder?
        return True
    
    for i in range(1,len_ladder-1):
        if ladder[i] != (
            (ladder[i-1]+ladder[i+1]) // 2
        ):
            return False
    return True


result = []
for _ in range(int(input())):
    len_ladder = int(input())
    ladder = list(
        map(int,input().split())
    )
    if is_fabulosa(ladder):
        result.append("YES")
    else:
        ...

