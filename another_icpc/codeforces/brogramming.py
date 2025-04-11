"""
>>> x = 56
>>> n = 4
>>> mask = (1 << 4) - 1
>>> temp = x & mask
>>> temp
8
>>> a(temp)
'1000'
>>> y = 0
>>> y = y << n
>>> y |= mask
>>> y
15
>>> a(y)
'1111'
>>> y = 2
>>> y = y << n
>>> y
32
>>> y = y | temp
>>> y
40
>>> a(y)
'101000'
>>>
"""
import sys
from io import StringIO

for_input = """1
6
111000
"""



is_all_one = lambda x : x+1 > 0 and (x+1 & (x)) == 0

def brogramming_contest_bitshift(test_cases):
    results = []
    
    for s in test_cases:
        num = int(s, 2)
        t = 0

        while not is_all_one(t) and num != 0:
            ...
    
    return results

t = int(input().strip())  
test_cases = []
for _ in range(t):
    n = int(input().strip())  
    s = input().strip()
    test_cases.append(s)

results = brogramming_contest_bitshift(test_cases)
for res in results:
    print(res)
