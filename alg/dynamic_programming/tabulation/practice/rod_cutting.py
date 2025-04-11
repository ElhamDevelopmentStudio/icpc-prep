import sys
from io import StringIO

input_string = """4
2 5 7 8
"""


"""
  2 5 7 8

0 1 2 3 4
0 2 5 7 10

i = 5
1 => 5

cost = 2
j = 1
cost + dp[] 

"""



sys.stdin = StringIO(input_string)

input = sys.stdin.readlines()
ptr = 0

length = int(input[ptr]); ptr+=1

prices = list(map(int,input[ptr].split()))

dp = [0] * (length+1)

for i in range(1,length+1):
    for j in range(1,i+1):
        cost = prices[j-1]
        dp[i] = max(
            cost+dp[i-j],
            dp[i]
        )

print(*dp)
print(dp[length])



