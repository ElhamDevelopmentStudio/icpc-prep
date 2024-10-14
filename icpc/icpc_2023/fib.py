import sys
from io import StringIO

input_ ="""2
2
7
"""

sys.stdin = StringIO(input_)

for _ in range(int(input())):
    num = int(input())
    a = 0
    b = 1
    for i in range(2,num+1):
        a,b=b,a+b

    print(b)
