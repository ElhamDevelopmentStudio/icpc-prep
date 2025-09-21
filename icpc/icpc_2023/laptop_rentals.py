import sys
from io import StringIO
test_input = """1
6
0 2
4 6
0 4
7 8
9 11
3 10
"""


sys.stdin = StringIO(test_input)


for _ in range(int(input())):
    amount_of_times = int(input())
    res = []
    for _ in range(amount_of_times):
        a,b = list(map(int,input().split()))
        res.append((a,+1))
        res.append((b,-1))

    res.sort(key=lambda x : x[0])
    result = float("-inf")
    counter = 0
    for comp,time in res:
        counter += time
        result = max(result,counter)

    print(result)

