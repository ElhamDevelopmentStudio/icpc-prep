import sys
from io import StringIO
from functools import reduce
test_input = """1
3
1110001101
1010101011
0000000011
"""

"""
First Match:
1 1 1 0 0 0 1 1 0 1
1 0 1 0 1 0 1 0 1 1
- W - - L - - W L -

4


0 1 0 0 1 0 0 1 1 0 -> Result of the first Match
0 0 0 0 0 0 0 0 1 1
- W - - W - - W - L

4


"""


sys.stdin = StringIO(test_input)


for _ in range(int(input())):
    num_of_matches = int(input())

    numbers = []
    for _ in range(num_of_matches):
        numbers.append(int(input(),2))

    bitwise_xor = lambda x,y : x^y
    result = reduce(bitwise_xor,numbers)
    print(bin(result)[2:].count("1"))
