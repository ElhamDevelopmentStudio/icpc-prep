import sys
from io import StringIO

input_ = """1
5,5,3,9,2
3,6,7,2,1
True
"""


sys.stdin = StringIO(input_)


for _ in range(int(input())):
    a = list(map(int,input().split(",")))
    b = list(map(int,input().split(",")))
    is_max = (input() == "True") 

    if is_max:
        result = 0
        a.sort()
        b.sort(reverse=True)
        for ridea,rideb  in zip(a,b):
            result += max(ridea,rideb)
        print(result)
    else:
        result = 0 
        a.sort()
        b.sort()
        for ridea,rideb  in zip(a,b):
            result += min(ridea,rideb)
        print(result)
