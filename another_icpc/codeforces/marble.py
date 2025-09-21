import sys
from io import StringIO

input_string = """4 2 1
2 3 4 1
"""



sys.stdin = StringIO(input_string) 

n,s,t = list(map(int,input().split()))
p = list(map(int,input().split()))

if s==t:
    print(0)
else:
    seen = set()
    marble = s-1
    count = 0
    result = -1
    while marble not in seen:
        count += 1
        if p[marble] == t:
            result = count 
            break
        seen.add(marble)
        marble = p[marble] -1
    print(result)
