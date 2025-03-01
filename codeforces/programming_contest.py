import sys
from io import StringIO

for_input = """1
6
111000
"""
sys.stdin = StringIO(for_input)

def brogramming_contest_bitshift(test_cases):
    results = []
    
    for s in test_cases:
        # Convert binary string to an integer
        num = int(s, 2)

        # Right-shift by one and XOR to find differences
        transitions = num ^ (num >> 1)
        
        # Count how many '10' patterns (bits that go from 1 to 0)
        moves = 0
        while transitions:
            if transitions & 3 == 2:  # Pattern '10' (binary 10 = decimal 2)
                moves += 1
            transitions >>= 1

        results.append(moves)
    
    return results


# Example Input
t = int(input().strip())  # Number of test cases
test_cases = []
for _ in range(t):
    n = int(input().strip())  # Length of binary string
    s = input().strip()
    test_cases.append(s)

# Compute and print results
results = brogramming_contest_bitshift(test_cases)
for res in results:
    print(res)
