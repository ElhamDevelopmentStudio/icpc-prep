"""
0101000110

{
    
}
"""

from collections import defaultdict
import sys
from io import StringIO

input_string = """1
10
0101000110
"""

sys.stdin = StringIO(input_string)

#s = input()

def find_indices(N, S):
    zeros = []
    ones = []

    for idx, char in enumerate(S, 1):
        if char == '0':
            zeros.append(idx)
        else:
            ones.append(idx)

    zero_sum_map = {} 
    for i in range(len(zeros)):
        for j in range(i + 1, len(zeros)):
            s = zeros[i] + zeros[j]
            if s not in zero_sum_map:
                zero_sum_map[s] = (zeros[i], zeros[j])
    
    for i in range(len(ones)):
        for j in range(i + 1, len(ones)):
            s = ones[i] + ones[j]
            if s in zero_sum_map:
                zero_pair = zero_sum_map[s]
                if (zero_pair[0] != ones[i] and zero_pair[0] != ones[j] and
                    zero_pair[1] != ones[i] and zero_pair[1] != ones[j]):
                    return zero_pair[0], zero_pair[1], ones[i], ones[j]
    
    return -1

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    result = find_indices(N, S)
    if result == -1:
        print(-1)
    else:
        print(result[0], result[1], result[2], result[3])
