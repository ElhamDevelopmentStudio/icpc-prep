"""


n = 3
S = 6


a = [3 3 6]

3 3

subsequence = 6

1 1
3

1 2
3 3 = 1

2 2
3 = 0

1 3
3 3 6 => 2

2 3
3 6 => 1

3 3
6 => 1

5

1 1
1 2
2 2
1 3
2 3
3 3

"""

import sys
from io import StringIO


input_string = """3 6
3 3 6
"""


sys.stdin = StringIO(input_string)


n,S = list(map(int,input().split()))
