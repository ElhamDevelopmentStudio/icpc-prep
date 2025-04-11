"""
cc
"""

"""
0 -> ca$hca$h
1 -> c$c$
2 -> ch$
3 -> cc
"""

import sys
from io import StringIO

input_string = """3
$f$f$f
$f
"""

sys.stdin = StringIO(input_string)



k = int(input())
S = input()
J = input()

def get_s(s,i):
    len_s = len(s)
    res = ""
    curr_index = 0
    while curr_index < len_s:
        res += s[curr_index]
        #print(f"curr res {res} and curr_index {curr_index}")
        curr_index+=i+1
    #print(f"returning {res}")
    return res



def solve(s,j):
    def inside_solve(i):
        len_j = len(j)
        cur_iter = 0
        len_s = len(s)
        while cur_iter < len_j and i < len_s and s[i] == j[cur_iter]:
            i+=1
            cur_iter += 1

        #print(f"curr_iter is {cur_iter} and len_j is {len_j} and s is {s[i]} and j is {j[cur_iter]}")
        is_solve = cur_iter == len_j
        return is_solve,cur_iter

    res = 0
    for i in range(len(s)):
        if s[i] == j[0]:
            solved,cur_iter = inside_solve(i)
            if solved:
                res += 1
                i += cur_iter
    return res





s_list = [S]
for i in range(1,k+1):
    s_list.append(
        get_s(S,i)
    )
result = []
for s in s_list:
    result.append(
            solve(s,J)
    )

print(
    "\n".join([str(x) for x in result])
)


