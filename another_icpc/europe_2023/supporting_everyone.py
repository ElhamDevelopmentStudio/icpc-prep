import sys


from io import StringIO

input_string = """7 6
3
1 4 5
3
1 4 5
3
1 4 5
3
3 4 5
3
3 4 5
3
3 4 5
3
2 5 6
"""


"""

5 -> 5
4 -> 5
1 -> 3
3 -> 3
2 -> 1
6 -> 1




"""

sys.stdin = StringIO(input_string)


n,m = list(
    map(int, input().split()
))

countries = []

for _ in range(n):
    _ = int(input())
    countries.append(
        list(map(
            int,input().split()
        ))
    )

print(*countries)
