import sys
from io import StringIO

print = sys.stdout.write


input_string = """1
6
"""



"""
200 600 400 100 200



"""


sys.stdin = StringIO(input_string)

lines = sys.stdin.readlines()
ptr = 0


def solve(n):
    r,c = 1,n-1


t = int(lines[ptr])
ptr+=1


for i in range(t):
    n = int(lines[ptr])
    ptr+=1

    res = solve(n)
    print(res)

