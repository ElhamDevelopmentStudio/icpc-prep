import sys
from io import StringIO
from functools import reduce
from math import gcd

print = sys.stdout.write


input_string = """3
1000 1000 1000 1000 1000
1 1 1 1 100000000000
200 600 400 100 200
"""



"""
200 600 400 100 200



"""


sys.stdin = StringIO(input_string)

lines = sys.stdin.readlines()
ptr = 0

t = int(lines[ptr])
ptr+=1

def solve(s):
    min_s = min(s)
    diffs = [s_ - min_s for s_ in s]

    gcd_val = reduce(gcd,diffs)

    if gcd_val % 3 == 0:
        return "YES"
    else:
        return "NO"

for i in range(t):
    #print(lines[ptr])
    s = list(map(int,lines[ptr].split()))
    res = solve(s)
    print(f"{res}\n")
    ptr+=1

