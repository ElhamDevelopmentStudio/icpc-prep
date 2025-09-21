import sys
from io import StringIO

test_input = """3
4 10
2 13 4 16
5 8
9 3 8 8 4
4 6
1 2 3 4
"""
sys.stdin = StringIO(test_input)

for _ in range(int(input())):
    length,max_height = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    count = 0
    for num in nums:
        if num > max_height:
            count += 1

    print(count)
