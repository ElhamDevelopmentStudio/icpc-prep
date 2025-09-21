import sys
from io import StringIO

input_string = """4
1 3
2 3
"""

sys.stdin = StringIO(input_string)


n = int(input())
nodes = [False] * n


a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

if (a < c < b < d) or (c < a < d < b):
    print(4)  
else:
    print(3) 
