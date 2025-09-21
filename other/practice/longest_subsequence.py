import sys
from io import StringIO

"""
0 0 0 0 0 0 0 0
"""
input_string = """10, 9, 2, 5, 3, 7, 101, 18
"""

sys.stdin = StringIO(input_string)

nums = list(map(int,input().split(",")))


n = len(nums)

dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n+1):
    ...
