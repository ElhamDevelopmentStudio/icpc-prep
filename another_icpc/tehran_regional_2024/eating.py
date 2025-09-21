import sys
from io import StringIO


input_string = """3
1 1
5
6
4 4
1 5 4 11
8
13
16
15
10 9
10 4 3 9 7 4 6 1 9 4
2
6
5
6
9
8
6
2
7
"""

sys.stdin = StringIO(input_string)


for _ in range(int(input())):
    n,q = list(map(int,input().split()))
    mars = list(map(int,input().split()))
    scores = []
    for q in range(q):
        number = int(input())
        score = 0
        mars_ma = mars.copy()
        mars_ma.append(number)
        while len(mars_ma) >= 2:
            if mars_ma[-1] >= mars_ma[-2]:
                xor_shan = mars_ma[-1] ^ mars_ma[-2]
                mars_ma.pop()
                mars_ma.pop()
                mars_ma.append(xor_shan)
                score += 1
            else:
                break 
        scores.append(score)
        score = 0
    print(*scores)  







